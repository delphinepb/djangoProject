#!/bin/bash
#pour pouvoir exécuter le fichier bash, il faut le placer dans le répertoire de travail GIT ou le rendre global

# récupérer la branche courrante et push
current_branch=$(git branch --show-current)

# git pull
git pull origin "$current_branch"
echo '\n'

# récuperer le message passé en argument
message="$1"

# ajouter tous les changements
git add .
echo "> Tous les fichiers sont ajoutés. \n"

# ajouter le commit avec le message
git commit -m "$message"
echo "> Commit ajouté avec le message: '$message' \n"

# git push
git push origin "$current_branch"
echo "> Changement poussé sur la branche '$current_branch'"
