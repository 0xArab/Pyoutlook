
# @xAltmime

try:

    import requests,re
except ImportError:
       print("  [+] install requests [+] ")

"""
 - Microsoft Outlook, or simply Outlook, is a personal information manager from Microsoft, available as a part of the Microsoft Office suite. Primarily an email application, it also includes a calendar, task manager, contact manager, note taking, journal, and web browsing. 
 - It can be used as a stand-alone application, or can work with Microsoft Exchange Server and Microsoft SharePoint Server for multiple users in an organization, such as shared mailboxes and calendars, Exchange public folders, SharePoint lists, and meeting schedules. Microsoft has also released mobile applications for most mobile platforms, including iOS and Android. Developers can also create their own custom software that works with Outlook and Office components using Microsoft Visual Studio.[6] In addition, Windows Phone devices can synchronize almost all Outlook data to Outlook Mobile. 
 - In March 2020 Microsoft has announced the launch of a series of new features to appeal to business customers of its Teams platform. Microsoft ends February with a new set of features for its Teams platform
 - chat and collaboration module now includes more efficient and more integrated waypoints, designed to simplify group work for companies and encourage them to adopt the Microsoft platform, which aims to become the chat platform of company par excellence.
 - The main new feature, the integration of Teams and Outlook, which means that users can now move an email conversation directly from Outlook to a Teams chat by clicking a button, but also share a conversation from Teams to an email on Outlook. Microsoft has also added the ability to assign a tag to members of an organization so that users can better target their messages

"""
class outlook:
        """  
             - Main informations  
               We want to make this variables available to everyone. 
        """

        SESSION = requests.Session()
        URL_OUTLOOK = "https://login.live.com/"
        UUID_HEADER = ""
        URL_LOGIN = "https://login.live.com/GetCredentialType.srf?uaid="


        def __init__(self,Email):
              self.Email_outlook = Email
                    
        """ set uuid Because we want to use it again."""
        def set_uuid():
                self.request_uuid = self.SESSION.get(URL_OUTLOOK)
                self.UUID_HEADER = self.request_uuid.cookies['uaid']

                if self.UUID_HEADER:
                     return True
                else:
                     return False

       """  universally unique identifier 
               - UUID) is a 128-bit number used to identify information in computer systems. The term globally unique identifier (GUID) is also used
               - When generated according to the standard methods, UUIDs are for practical purposes unique
               - Their uniqueness does not depend on a central registration authority or coordination between the parties generating them, unlike most other numbering schemes
               - anyone can create a UUID and use it to identify something with near certainty that the identifier does not duplicate one that has already been, or will be, created to identify something else. Information labeled with UUIDs by independent parties can therefore
       """
        def get_uuid(self):
                return self.UUID_HEADER

        """ - This is Microsoft Flow - Token Authentication """
        def get_flow(self):
                return re.findall('<input type="hidden" name="PPFT" id="i0327" value=(.*?)>',self.request_uuid.text)[0].replace('""/','').replace('"',"")
        
        def data_requests():

                return  {"username":self.Email_outlook,"uaid":self.get_uuid(),"isOtherIdpSupported":"false","checkPhones":"false","isRemoteNGCSupported":"true","isCookieBannerShown":"false",
                   "isFidoSupported":"false",
                         "forceotclogin":"false",
                    "otclogindisallowed":"false",
                          "isExternalFederationDisallowed":"false",
                   "isRemoteConnectSupported":"false",
                          "federationFlags":3,
                   "isSignup":"false",
                          "flowToken":self.get_flow()
                        }
        """ Login and get data of others functions """

        def Login_to_outlook(self):
                get_uuid_and_url_login = self.URL_LOGIN + str ( self.get_uuid() )
                return session.post(URL_LOGIN,json=self.data_requests()).text

       """ We check the content that's in function Login_to_outlook  """ 
        def respone_of_login(self)
                if '"IfExistsResult":0' in self.Login_to_outlook():
                        print( "   This Email exists  !" )
                else:
                        print("[+++++++++] Email Not exists ")
                

        
        
        
Login("looolis@outlook.com")
