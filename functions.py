###Mes fonctions

#creer l'url avec son checksum

import hashlib

def checksumUrl(queryString,action,secret):
	#1. Create the entire query string for your API call without the checksum parameter "name=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444"
	#2. Prepend the call name to your string "createname=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444"
	#3. Now, append the shared secret to your string  "createname=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444639259d4-9dd8-4b25-bf01-95f9567eaf4b"
	checksum = action+queryString+secret
	#4. Now, find the SHA-1 sum for that string "1fcbb0c4fc1f039f73aa6d697d2db9ba7f803f17"
	sha1 = hashlib.sha1(checksum)
	sha1Hex = sha1.hexdigest()
#	print "debug sha1hex = "+sha1Hex
	#5. Add a checksum parameter to your query string that contains this checksum "name=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444&checksum=1fcbb0c4fc1f039f73aa6d697d2db9ba7f803f17"
	finalChecksumUrl = action+"?"+queryString+"&checksum="+sha1Hex
	return finalChecksumUrl
