import instaloader

username = "kullanıcı_ad"
password = "şifre"

instagram = instaloader.Instaloader()

try:
    instagram.login(username, password)

    profile = instaloader.Profile.from_username(instagram.context, username)

    followers = profile.get_followers()
    following = profile.get_followees()

    followers_list = [follower.username for follower in followers]
    following_list = [followee.username for followee in following]

    count = 0
    for followed_username in following_list:
        if followed_username not in followers_list:
            print(followed_username, "kullanicisi seni takip etmiyor")
            count += 1

    print("Sana geri takip yapmayan kullanici sayisi:", count)

except instaloader.exceptions.InstaloaderException as e:
    print("Hata:", str(e))
