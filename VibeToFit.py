import tkinter as tk
from tkinter import messagebox
import datetime

favorites = []

def get_current_season():
    month = datetime.datetime.now().month
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "autumn"

def recommend_color(moods):
    mood_to_color = {
        "happy": "yellow",
        "sad": "blue",
        "angry": "red",
        "stressed": "blue",
        "relaxed": "green",
        "energetic": "red",
        "calm": "blue",
        "serious": "black",
        "caring": "pink"
    }
    colors = [mood_to_color.get(m.strip()) for m in moods if m.strip() in mood_to_color]
    return colors if colors else None

def suggest_outfit(color, style, gender, season):
    outfit_dict = {
        "yellow": {
            "casual": {"male": "yellow t-shirt with shorts", "female": "flowy yellow summer dress"},
            "formal": {"male": "yellow shirt with beige chinos", "female": "mustard yellow sheath dress"},
            "sporty": {"male": "yellow dry-fit and joggers", "female": "yellow tank top with black leggings"}
        },
        "blue": {
            "casual": {"male": "blue hoodie and jeans", "female": "blue denim shirt dress"},
            "formal": {"male": "blue shirt with grey trousers", "female": "navy blue pencil dress"},
            "sporty": {"male": "blue gym tee and shorts", "female": "blue activewear set (sports bra & leggings)"}
        },
        "red": {
            "casual": {"male": "red polo shirt with black jeans", "female": "red wrap dress with sneakers"},
            "formal": {"male": "red blazer and white shirt", "female": "elegant red midi dress"},
            "sporty": {"male": "red jersey and track pants", "female": "red sports tee with shorts"}
        },
        "green": {
            "casual": {"male": "green tee and joggers", "female": "green boho maxi dress"},
            "formal": {"male": "olive green shirt and trousers", "female": "dark green bodycon dress"},
            "sporty": {"male": "green athletic tee and shorts", "female": "green yoga outfit"}
        },
        "black": {
            "casual": {"male": "black t-shirt and jeans", "female": "black casual jumpsuit"},
            "formal": {"male": "black suit and tie", "female": "classic black evening gown"},
            "sporty": {"male": "black tracksuit", "female": "black gym co-ord set"}
        },
        "pink": {
            "casual": {"male": "pink shirt and jeans", "female": "light pink floral dress"},
            "formal": {"male": "light pink shirt with navy pants", "female": "blush pink formal dress"},
            "sporty": {"male": "pink tee and joggers", "female": "pink workout set"}
        }
    }

    item = outfit_dict.get(color, {}).get(style, {}).get(gender, None)
    if not item:
        return "an outfit in your favorite color and style"

    if season == "summer" and color == "black":
        return f"{item} (⚠️ consider a lighter color for summer)"
    elif season == "winter" and style == "casual":
        return f"{item} with a jacket or sweater"
    else:
        return item

def generate_recommendation():
    moods = mood_entry.get().lower().split(",")
    style = style_var.get()
    gender = gender_var.get()

    colors = recommend_color(moods)
    if not colors:
        messagebox.showerror("Invalid Mood", "❌ Please enter valid moods like: happy, sad, relaxed, etc.")
        return

    season = get_current_season()
    results = []

    for color in colors:
        outfit = suggest_outfit(color, style, gender, season)
        results.append(f"🎨 Mood Color: {color.capitalize()}\n👕 Outfit: {outfit}")

    result_text.set("\n\n".join(results))

def save_favorite():
    fav = result_text.get()
    if fav:
        favorites.append(fav)
        messagebox.showinfo("Saved", "✅ This outfit has been added to your favorites!")

def show_favorites():
    if favorites:
        fav_window = tk.Toplevel(root)
        fav_window.title("⭐ Saved Favorites")
        fav_window.configure(bg="black")
        fav_text = tk.Text(fav_window, width=60, height=15, wrap="word", bg="black", fg="white")
        fav_text.pack(padx=10, pady=10)
        fav_text.insert(tk.END, "\n\n".join(favorites))
    else:
        messagebox.showinfo("Favorites", "😕 You have no saved outfits yet.")

# ------------------- GUI Layout -------------------
root = tk.Tk()
root.title("Color Psychology Outfit Recommender")
root.geometry("430x520")
root.configure(bg="black")
root.resizable(False, False)

tk.Label(root, text="👗 Color Psychology Outfit Recommender", font=("Segoe UI", 14, "bold"),
         bg="black", fg="white").pack(pady=10)

tk.Label(root, text="🧠 Enter Your Mood(s) (comma-separated):", font=("Segoe UI", 10),
         bg="black", fg="white").pack(pady=(10, 0))
mood_entry = tk.Entry(root, width=40, font=("Segoe UI", 10), bg="#333", fg="white", insertbackground="white")
mood_entry.pack(pady=5)

tk.Label(root, text="🧥 Select Your Style:", font=("Segoe UI", 10), bg="black", fg="white").pack(pady=(10, 0))
style_var = tk.StringVar(value="casual")
tk.OptionMenu(root, style_var, "casual", "formal", "sporty").pack(pady=5)

tk.Label(root, text="🚻 Select Your Gender:", font=("Segoe UI", 10), bg="black", fg="white").pack(pady=(10, 0))
gender_var = tk.StringVar(value="female")
tk.OptionMenu(root, gender_var, "female", "male").pack(pady=5)

tk.Button(root, text="🎯 Get Outfit Recommendation", command=generate_recommendation,
          font=("Segoe UI", 10, "bold"), bg="#6ec6ff", fg="black").pack(pady=15)

result_frame = tk.Frame(root, bd=2, relief="sunken", padx=10, pady=10, bg="#1a1a1a")
result_frame.pack(pady=5, padx=10, fill="both")
result_text = tk.StringVar()
tk.Label(result_frame, textvariable=result_text, font=("Segoe UI", 10), wraplength=380,
         justify="left", bg="#1a1a1a", fg="white").pack()

tk.Button(root, text="⭐ Save to Favorites", command=save_favorite,
          font=("Segoe UI", 9), bg="#333", fg="white").pack(pady=(15, 5))
tk.Button(root, text="📁 Show Favorites", command=show_favorites,
          font=("Segoe UI", 9), bg="#444", fg="white").pack()

root.mainloop()
