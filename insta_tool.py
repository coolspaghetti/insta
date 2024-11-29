import instaloader
import json
import time

# initialize instaloader
loader = instaloader.Instaloader()

# target account
target_account = input("Enter the account username: ")

# fetch profile
profile = instaloader.Profile.from_username(loader.context, target_account)

# open file to save captions
with open(f"{target_account}_captions.json", "w", encoding="utf-8") as file:
    captions = []
    for post in profile.get_posts():
        captions.append({
            "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
            "caption": post.caption or ""
        })

        # delay to avoid rate-limiting
        time.sleep(5) # 5-second delay

    json.dump(captions, file, ensure_ascii=False, indent=4)

print(f"Captions saved to {target_account}_captions.json")
