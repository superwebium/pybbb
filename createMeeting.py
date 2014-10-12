# -*- coding: utf-8 -*-

import urllib, random
from fonctions import checksumUrl

#je declare les variables variables

curServ = "http://test-install.blindsidenetworks.com/bigbluebutton/api/"
curSecret = "8cd8ef52e8e101574e400365b55e11a6"
curMeetingId = "aze"
curName = raw_input("Nom de votre conférence :")
curAttendedPw = raw_input("Mot de passe des invités :")
curModeratorPw = raw_input("Mot de passe de modérateur :")
curFullName = raw_input("Entrer votre nom :")

createQuery = "name="+curName+"&meetingID="+curMeetingId+"&attendeePW="+curAttendedPw+"&moderatorPW="+curModeratorPw
urlCreateQuery = curServ+checksumUrl(createQuery,"create",curSecret)
print curServ+checksumUrl(createQuery,"create",curSecret)
urllib.urlopen(urlCreateQuery)
