MISE A JOUR IMPORTANTE

1) index.html a été modifié pour :
- supprimer le bouton de téléchargement des réponses
- ne plus afficher score ni bonnes réponses aux étudiants
- ajouter Niveau d'étude
- ajouter Apprenant du chinois ?
- cacher HSK / HSKK / Année d'étude en chinois quand la personne n'apprend pas le chinois
- ajouter un mode test technique ?debug=1
- confirmer l'enregistrement dans Google Sheets

2) Code.gs doit être collé dans Apps Script puis redéployé comme Web App.

3) Les fichiers bonnes_reponses_exp1_2.json et bonnes_reponses_exp4.json ont été retirés du dossier public.
Les clés de réponses sont maintenant dans Code.gs côté serveur.
C'est important pour éviter que les étudiants récupèrent les bonnes réponses depuis le navigateur.

4) Après avoir collé Code.gs :
- Enregistrer
- Déployer > Nouvelle version / Gérer les déploiements
- Type : Application Web
- Exécuter en tant que : vous-même
- Accès : Toute personne disposant du lien
- Mettre à jour le déploiement

5) Test technique :
- ouvrir le site avec ?debug=1
- cliquer sur "Lancer le test automatique Google Sheets"
- vérifier que les lignes marquées Test_Mode = OUI arrivent dans les vraies feuilles
- supprimer ensuite ces lignes de test

6) Option recommandée :
- dans Code.gs, remplissez SPREADSHEET_ID avec l'ID exact du Google Sheet
- c'est plus robuste que getActiveSpreadsheet() si jamais le script bouge
