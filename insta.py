import instaloader, sys

def banner():
        print("""
\033[1;32m.___         _________
\033[1;32m|   | ____  /   _____/ ________________  ______   ____
\033[1;32m|   |/    \ \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \ 
\033[1;33m|   |   |  \/        \  \___|  | \// __ \|  |_> >  ___/
\033[1;33m|___|___|  /_______  /\___  >__|  (____  /   __/ \___  >
         \033[1;33m\/        \/     \/           \/|__|        \/\033[0m
\033[41m# Coded by Black Eye Community\033[1;0m | \033[42mgithub.com/rohmadhidayah\033[0m
""")

banner()

x = instaloader.Instaloader()

#Login dulu
try:
	uname = input("\033[1;36mUsername: \033[0;30m")
	passwd = input("\033[1;36mPassword: \033[0;30m")

	x.login(uname,passwd)
	print("\033[1;32mLogin successful...")

except:
	print("\033[1;31mLogin failed!")
	sys.exit()

#Suruh user masukin username target
username = input("\033[1;32mMasukkan username: \33[0m")
if username == "":
	print("\033[1;31mUser not found!")
	sys.exit()

y = instaloader.Profile.from_username(x.context, username)

print("\033[1;32mUsername : \033[0m",y.username)
print("\033[1;32mID : \033[0m",y.userid)
print("\033[1;32mNama : \033[0m",y.full_name)
print("\033[1;32mTerverifikasi : \033[0m",y.is_verified)
print("\033[1;32mDiprivasi : \033[0m",y.is_private)
print("\033[1;32mAkun bisnis : \033[0m",y.is_business_account)
print("\033[1;32mNama kategori bisnis : \033[0m",y.business_category_name)
print("\033[1;32mBiografi : \033[0m",y.biography)
print("\033[1;32mPengikut : \033[0m",y.followers)
print("\033[1;32mMengikuti : \033[0m",y.followees)
print("\033[1;32mURL foto profil : \033[0m",y.profile_pic_url)
print("\033[1;32mURL eksternal : \033[0m",y.external_url)
print("\033[1;32mPostingan : \033[0m",y.mediacount)
print("\033[1;32mIGTV : \033[0m",y.igtvcount)
print("\033[1;32mMemiliki cerita yang dapat dilihat : \033[0m",y.has_viewable_story)
print("\033[1;32mMemiliki cerita publik : \033[0m",y.has_public_story)
print("\033[1;32mMemiliki sorotan : \033[0m",y.has_highlight_reels)
print("\033[1;32mDiikuti user lain : \033[0m",y.followed_by_viewer)
print("\033[1;32mMengikuti user lain : \033[0m",y.follows_viewer)
print("\033[1;32mDiblokir user lain : \033[0m",y.blocked_by_viewer)
print("\033[1;32mPernah memblokir user lain : \033[0m",y.has_blocked_viewer)
print("\033[1;32mDiminta user lain : \033[0m",y.requested_by_viewer)
print("\033[1;32mMeminta user lain : \033[0m",y.has_requested_viewer)
for i in y.get_followers():
	print("\033[1;32mPengikut : \033[0m",i)
for i in y.get_followees():
	print("\033[1;32mMengikuti : \033[0m",i)
for i in y.get_similar_accounts():
	print("\033[1;32mAkun serupa : \033[0m",i)
