import instaloader

loader = instaloader.Instaloader()

reel_url = input("Enter the url of the reel: ")

shortcode = reel_url.split('/')[-2]

# download the reel
try:
    loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target="reels")
    print("Reel downloaded successfully!")
except Exception as e:
    print(f"Error downloading reel: {e}")