from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des utilisateurs fictifs pour la démonstration
utilisateurs = {
    'utilisateur1': 'motdepasse1',
    'utilisateur2': 'motdepasse2'
}

@app.route('/', methods=['GET', 'POST'])
def connexion():
    message = ''

    if request.method == 'POST':
        nom_utilisateur = request.form['nom_utilisateur']
        mot_de_passe = request.form['mot_de_passe']

        if nom_utilisateur in utilisateurs and utilisateurs[nom_utilisateur] == mot_de_passe:
            # Authentification réussie, rediriger vers une page sécurisée
            return redirect(url_for('page_securisee'))
        else:
            message = 'Nom d\'utilisateur ou mot de passe incorrect.'

    # Si la méthode est GET ou si l'authentification a échoué, afficher à nouveau la page de connexion
    return render_template('connexion.html', message=message)

@app.route('/page_securisee')
def page_securisee():
    return 'Bienvenue sur la page sécurisée!'

if __name__ == '__main__':
    app.run(debug=True)