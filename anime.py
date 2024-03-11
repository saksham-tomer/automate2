import webbrowser

arg = input("Enter your choise ---> \n"
       " 1-youtube \n"
       " 2-aniwatch \n"
       " 3-twitch \n"
       " 4-instagram \n"
       " 5-portfolio \n")

ar =int(arg)
match ar:
    case 1:
      url =  "youtube.com"
    case 2:
       url= "aniwatchtv.to"
    case 3:
       url =  "twitch.com"
    case 4:
       url = "instagram.com"
    case 5:
        url = "portfolio-website-seven-kappa.vercel.app"
    case _:
       print("wrong")


webbrowser.open(url)
