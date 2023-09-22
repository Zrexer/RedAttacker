#!/usr/bin/env python3

import os
import yourAuths
import yourKeys

class updater:
    def downloadLibs():
        print("[i] install colorama\n")
        os.system("pip install colorama")
        os.system("cls || clear")
        print("[i] install requests")
        os.system("pip install requests")
        os.system("cls || clear")
        print("[i] install pyfiglet")
        os.system("pip install pyfiglet")
        os.system("cls || clear")
        print("[i] install pyrubi")
        os.system("pip install pyrubi")
        os.system("cls || clear")
        print("[i] install rubiran")
        os.system("pip install rubiran")
        os.system("cls || clear")
        
class activity:
    global colorama
    global os
    global sys
    global pyfiglet
    global time
    import os
    import colorama
    import sys
    import pyfiglet
    import time

    def printBanner():
        os.system("cls || clear")
        #print(colorama.Fore.RED+pyfiglet.figlet_format("Red")+colorama.Fore.BLUE+"-"*55+"\n"+colorama.Fore.YELLOW+pyfiglet.figlet_format("Attacker"))
        #print(colorama.Fore.BLUE+"-"*55+colorama.Fore.WHITE)
        print(f"""
{colorama.Fore.MAGENTA}_______  _______  ______  
{colorama.Fore.YELLOW}(  ____ )(  ____ \(  __  \ 
{colorama.Fore.MAGENTA}| (    )|| (    \/| (  \  )
{colorama.Fore.YELLOW}| (____)|| (__    | |   ) |
{colorama.Fore.MAGENTA}|     __)|  __)   | |   | |
{colorama.Fore.YELLOW}| (\ (   | (      | |   ) |
{colorama.Fore.MAGENTA}| ) \ \__| (____/\| (__/  )
{colorama.Fore.YELLOW}|/   \__/(_______/(______/ 

{colorama.Fore.MAGENTA}     __                                           
{colorama.Fore.YELLOW}    / |                          /               
{colorama.Fore.MAGENTA}---/__|--_/_--_/_----__----__---/-__----__---)__-
{colorama.Fore.YELLOW}  /   |  /    /    /   ) /   ' /(     /___) /   )
{colorama.Fore.MAGENTA}_/____|_(_ __(_ __(___(_(___ _/___\__(___ _/_____
                                                 
{colorama.Fore.MAGENTA}

                                     |"|                 
                                    _|_|_          
                                    (o o)        
{colorama.Fore.RED}          ================{colorama.Fore.YELLOW}]{colorama.Fore.MAGENTA} Ooo-ooO--(_)--Ooo-ooO {colorama.Fore.YELLOW}[{colorama.Fore.RED}================


""")
            
    def checkArgv():
        try:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                activity.printBanner()
                print("USAGE: python3 nameFile.py [-h / --help] [-dp / --download-packs] [-i / --info]")
            elif sys.argv[1] == "-dp" or sys.argv[1] == "--download-packs":
                try:
                    updater.downloadLibs()
                except:pass
                finally:
                    os.system("cls || clear")
                    print(f'{colorama.Fore.GREEN}[{colorama.Fore.YELLOW}i{colorama.Fore.GREEN}]{colorama.Fore.WHITE} Finish Install')
                    time.sleep(3)
            
            else:pass
        except:pass
        
    def BombAccountAuthAndKey(auths, keys, lengthOfjl : int, targetGuid, message):
        global rubiran
        import rubiran
        for auth, key in auths, keys:              
            num = 0
            try:
                for l in lengthOfjl:

                    try:
                        app = rubiran.rubiran(auth=auth, privateKey=key)
                        print("\n"+"-"*15)
                        app.sendMessage(chat_id=targetGuid, text=message)
                        print("[i] message sended")
                        num += 1
                        print(f"number of mission: {num}")
                        print("-"*15)
                    except Exception as EJSL:
                        print(f"Base Error: {EJSL}")
                        pass
                            
            except Exception as EF1:
                print(f"Error For: {EF1}")
                pass
            
    def BombGapWithAuthAndKey(auths, keys, lengthOfjl: int, linkGap, guidGap, message):
        for auth, key in auths, keys:
            num = 0

            try:
                for l in lengthOfjl:

                    try:
                        app = rubiran.rubiran(auth=auth, privateKey=key)
                        app.joinGroup(link=linkGap)
                        print("\n"+"-"*15)
                        print("[i] join")
                        app.sendMessage(chat_id=guidGap, text=message)
                        print("[i] message sended")
                        app.leaveGroup(chat_id=guidGap)
                        print("[i] bot leaved gap")
                        num += 1
                        print(f"[i] number of mission: {num}")
                        print("-"*15)
                    except Exception as EJSL:
                        print(f"Base Error: {EJSL}")
                        pass
                            
            except Exception as EF1:
                print(f"Error For: {EF1}")
                pass

    def BombAccountWithLogin(sessionName, lengthOfjl: int, targetGuid, message):
        global pyrubi
        import pyrubi 

        try:
            for l in lengthOfjl:
                try:
                    app = pyrubi.Bot(session=sessionName)
                    print("\n"+"-"*15)
                    app.send_text(chat_id=targetGuid, text=message)
                    print("[i] message sended")
                    num += 1
                    print(f"number of mission: {num}")
                    print("-"*15)
                except Exception as EJSL:
                    print(f"Base Error: {EJSL}")
                    pass
                        
        except Exception as EF1:
            print(f"Error For: {EF1}")
            pass

    def BombGapWithLogin(sessionName, lengthOfjl: int, linkGap, guidGap, message):
        num = 0

        try:
            for l in lengthOfjl:

                try:
                    app = pyrubi.Bot(session=sessionName)
                    app.join_group(group_link=linkGap)
                    print("\n"+"-"*15)
                    print("[i] join")
                    app.send_text(chat_id=guidGap, text=message)
                    print("[i] message sended")
                    app.leave_group(group_guid=guidGap)
                    print("[i] bot leaved gap")
                    num += 1
                    print(f"[i] number of mission: {num}")
                    print("-"*15)
                except Exception as EJSL:
                    print(f"Base Error: {EJSL}")
                    pass
                        
        except Exception as EF1:
            print(f"Error For: {EF1}")
            pass





class MainActivity:
    def main():
        os.system("cls || clear")
        activity.checkArgv()
        activity.printBanner()
        while 1:
            try:
                usr = str(input(f"\n{colorama.Fore.MAGENTA}#{colorama.Fore.RED}[{colorama.Fore.YELLOW}Red{colorama.Fore.RED}.{colorama.Fore.MAGENTA}Attacker{colorama.Fore.CYAN}:{colorama.Fore.WHITE} "))
                if usr == "-aaa" or usr == "--attack-account-auth":
                    msg = str(input(f"\n{colorama.Fore.RED}set {colorama.Fore.WHITE}message{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    target = str(input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} target guid{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    if target.startswith("https://web.rubika.ir/#c="):
                        linkInfo = target.replace("https://web.rubika.ir/#c=", "")
                        if linkInfo.startswith("g0") or linkInfo.startswith("c0"):
                            print(f"{colorama.Fore.RED}Invalid Link: Please set a guid user not guid gap or guid channel !")
                            time.sleep(3)
                            MainActivity.main()
                        elif linkInfo.startswith("u0"):
                            lenght = input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} len (meghdar / مقدار ارسال) {colorama.Fore.YELLOW}>{colorama.Fore.WHITE} ")
                            try:
                                activity.BombAccountAuthAndKey(auths=yourAuths.allOfAuths, keys=yourKeys.allOfKeys, lengthOfjl=int(lenght), targetGuid=target, message=msg)
                            except:pass
                            finally:
                                print(f"{colorama.Fore.RED}Reset Script ...")
                                time.sleep(1)
                                MainActivity.main()
                                
                        else:
                            print(f"{colorama.Fore.RED}Invalid Guid !")
                            time.sleep(3)
                            MainActivity.main()
                                
                    else:
                        print(f"{colorama.Fore.RED}Invalid Link !")
                        time.sleep(3)
                        MainActivity.main()
                        
                elif usr == "-aga" or usr == "--attack-gap-auth":
                    msg = str(input(f"\n{colorama.Fore.RED}set {colorama.Fore.WHITE}message{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    target = str(input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} target guid{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    if target.startswith("https://web.rubika.ir/#c="):
                        linkInfo = target.replace("https://web.rubika.ir/#c=", "")
                        if linkInfo.startswith('u0') or linkInfo.startswith('c0'):
                            print(f"{colorama.Fore.RED}Invalid Link: Please set a guid user not guid gap or guid channel !")
                            time.sleep(3)
                            MainActivity.main()
                        elif linkInfo.startswith("g0"):
                            lenght = input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} len (meghdar / مقدار ارسال) {colorama.Fore.YELLOW}>{colorama.Fore.WHITE} ")
                            try:
                                activity.BombGapWithAuthAndKey(auths=yourAuths.allOfAuths, keys=yourKeys.allOfKeys, lengthOfjl=int(lenght), guidGap=target, message=msg)
                            except:pass
                            finally:
                                print(f"{colorama.Fore.RED}Reset Script ...")
                                time.sleep(1)
                                MainActivity.main()
                                
                        else:
                            print(f"{colorama.Fore.RED}Invalid Guid !")
                            time.sleep(3)
                            MainActivity.main()
                                
                    else:
                        print(f"{colorama.Fore.RED}Invalid Link !")
                        time.sleep(3)
                        MainActivity.main()
                        
                        
                        
                elif usr == "-aal" or usr == "--attack-account-login":
                    name = str(input(f"\n{colorama.Fore.RED}set{colorama.Fore.WHITE} name{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    msg = str(input(f"{colorama.Fore.RED}set {colorama.Fore.WHITE}message{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    target = str(input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} target guid{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    if target.startswith("https://web.rubika.ir/#c="):
                        linkInfo = target.replace("https://web.rubika.ir/#c=", "")
                        if linkInfo.startswith("g0") or linkInfo.startswith("c0"):
                            print(f"{colorama.Fore.RED}Invalid Link: Please set a guid user not guid gap or guid channel !")
                            time.sleep(3)
                            MainActivity.main()
                        elif linkInfo.startswith("u0"):
                            lenght = input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} len (meghdar / مقدار ارسال) {colorama.Fore.YELLOW}>{colorama.Fore.WHITE} ")
                            try:
                                activity.BombAccountWithLogin(sessionName=name ,lengthOfjl=int(lenght), targetGuid=target, message=msg)
                            except:pass
                            finally:
                                print(f"{colorama.Fore.RED}Reset Script ...")
                                time.sleep(1)
                                MainActivity.main()
                                
                        else:
                            print(f"{colorama.Fore.RED}Invalid Guid !")
                            time.sleep(3)
                            MainActivity.main()
                                
                    else:
                        print(f"{colorama.Fore.RED}Invalid Link !")
                        time.sleep(3)
                        MainActivity.main()
                        
                elif usr == "-agl" or usr == "--attack-gap-login":
                    name = str(input(f"\n{colorama.Fore.RED}set{colorama.Fore.WHITE} name{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    msg = str(input(f"{colorama.Fore.RED}set {colorama.Fore.WHITE}message{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    target = str(input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} target guid{colorama.Fore.YELLOW} >{colorama.Fore.WHITE} "))
                    if target.startswith("https://web.rubika.ir/#c="):
                        linkInfo = target.replace("https://web.rubika.ir/#c=", "")
                        if linkInfo.startswith('u0') or linkInfo.startswith('c0'):
                            print(f"{colorama.Fore.RED}Invalid Link: Please set a guid user not guid gap or guid channel !")
                            time.sleep(3)
                            MainActivity.main()
                        elif linkInfo.startswith("g0"):
                            lenght = input(f"{colorama.Fore.RED}set{colorama.Fore.WHITE} len (meghdar / مقدار ارسال) {colorama.Fore.YELLOW}>{colorama.Fore.WHITE} ")
                            try:
                                activity.BombGapWithLogin(sessionName=name, lengthOfjl=int(lenght), guidGap=target, message=msg)
                            except:pass
                            finally:
                                print(f"{colorama.Fore.RED}\nReset Script ...")
                                time.sleep(1)
                                MainActivity.main()
                                
                        else:
                            print(f"{colorama.Fore.RED}Invalid Guid !")
                            time.sleep(3)
                            MainActivity.main()
                                
                    else:
                        print(f"{colorama.Fore.RED}Invalid Link !")
                        time.sleep(3)
                        MainActivity.main()
                        
                
                elif usr == "cls" or usr == "clear" or usr == "c":
                    os.system("cls || clear")
                    MainActivity.main()
                    
                elif usr == "h" or usr == "help" or usr == "?":
                    print(f"""\n{colorama.Fore.WHITE}USAGE: attack the {colorama.Fore.YELLOW}account{colorama.Fore.WHITE} with {colorama.Fore.RED}auth {colorama.Fore.WHITE}and {colorama.Fore.RED}keys{colorama.Fore.WHITE}: -aaa / --attack-account-auth
       attack the {colorama.Fore.YELLOW}gap{colorama.Fore.WHITE} with {colorama.Fore.RED}auth {colorama.Fore.WHITE}and{colorama.Fore.RED} keys{colorama.Fore.WHITE}: -aga / --attack-gap-auth
                          
       attack the {colorama.Fore.YELLOW}account{colorama.Fore.WHITE} with {colorama.Fore.RED}login{colorama.Fore.WHITE}: -aal / --attack-account-login
       attack the {colorama.Fore.YELLOW}gap{colorama.Fore.WHITE} with {colorama.Fore.RED}login{colorama.Fore.WHITE}: -agl / --attack-gap-login

{colorama.Fore.RED}Note:{colorama.Fore.WHITE} set your auth and keys in "youAuths.py" and "youKeys.py" .
""")
                
                elif usr == "e" or usr == "exit":
                    print(f"{colorama.Fore.RED}\nExit{colorama.Fore.WHITE}")
                    exit()
                        
            except KeyboardInterrupt:
                print(f"\n\n{colorama.Fore.RED}Exit{colorama.Fore.WHITE}")
                exit()
        
MainActivity.main()
