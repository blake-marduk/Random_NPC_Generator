import tkinter as tk
from tkinter import ttk, scrolledtext
import random
import re

# --- DATA STRUCTURE ---
# All data for character generation is stored in this single dictionary.
CHARACTER_DATA = {
    "names": {
        "first_names": [
            'Elara', 'Bram', 'Renna', 'Kael', 'Seraphina', 'Gideon', 'Lyra', 'Orion',
            'Astrid', 'Joric', 'Faye', 'Roric', 'Isolde', 'Valerius', 'Maeve', 'Lucian',
            'Anya', 'Zane', 'Cora', 'Finnian', 'Eliza', 'Darian', 'Gwendolyn', 'Rhys',
            'Briar', 'Torvin', 'Lilith', 'Silas', 'Nia', 'Rowan', 'Kaelen'
        ],
        "last_names": [
            'Stonehand', 'Whisperwind', 'Ironfoot', 'Shadowalker', 'Silverwood', 'Stormrider',
            'Blackwater', 'Fireheart', 'Sunstrider', 'Moonshadow', 'Swiftbrook', 'Greycastle',
            'Nightshade', 'Starfall', 'Winterbourne', 'Deepwood', 'Ravencrest', 'Thornwall',
            'Oakhaven', 'Brightflame', 'Skyshield', 'Bronzebeard', 'Wildheart', 'Frostfang',
            'Ironhide', 'Shadowend', 'Grimshaw', 'Hawkeye', 'Redhammer', 'Lightbringer',
            'Steelgaze', 'Voidgazer', 'Quickquiver', 'Stonefist', 'Goldhand', 'Runeweaver',
            'Dreamwalker', 'Soulfire', 'Bloodmoon', 'Mistvale', 'Gravewind', 'Emberfall',
            'Rustedge', 'Greymane', 'Doomhammer', 'Shatterstone', 'Axebreaker', 'Windrunner',
            'Nightwind', 'Dawnsong'
        ],
    },
    "physical_traits": {
        "races": [
            'Human', 'Elf', 'Dwarf', 'Orc', 'Halfling', 'Gnome', 'Dragonborn',
            'Tiefling', 'Half-Elf', 'Half-Orc'
        ],
        "heights": [
            'Unusually Short', 'Short', 'Average Height', 'Tall', 'Imposingly Tall'
        ],
        "builds": [
            'Slender', 'Wiry', 'Athletic', 'Stocky', 'Muscular', 'Heavy-set', 'Gaunt', 'Lanky'
        ],
        "notable_features": [
            'a long scar over their left eye', 'a tattoo of a coiled serpent on their neck',
            'a chipped front tooth', 'unusually bright green eyes', 'a mechanical prosthetic hand',
            'a network of faint scars on their forearms', 'a single white streak in their hair',
            'one eye that is a different color from the other', 'an ornate silver ring they never remove',
            'a habit of constantly tapping their fingers', 'long, pointed ears for their race',
            'a brand mark on their shoulder', 'a missing finger on their right hand',
            'a perpetually smirking expression', 'a soft, melodic voice that is surprisingly disarming',
            'calloused hands that speak of hard labor', 'a faint dusting of freckles across their nose',
            'a piercing gaze that seems to look right through you', 'a slight limp when they walk',
            'an intricate hairstyle held with pins of carved bone', 'a collection of small, strange trinkets on their belt',
            'a weathered and worn leather satchel they always carry', 'a nervous twitch in their left eye',
            'fingernails stained with ink', 'a voice that is deeper than expected', 'a faint scent of ozone about them',
            'a silver locket that is always warm to the touch', 'a pair of well-worn spectacles perched on their nose',
            'a meticulously trimmed beard, braided with silver clasps', 'a subtle, almost unnoticeable shimmer to their skin',
            'a tendency to gesture wildly while talking', 'a quiet, observant nature, always watching',
            'a crude, self-inflicted tattoo on their wrist', 'a hoarse laugh', 'burn scars along one side of their face',
            'a jawline that could cut glass', 'eyes that seem older than their years', 'a penchant for humming ancient tunes',
            'a lucky coin they constantly flip', 'a set of perfectly white, sharp teeth',
            'a small, almost invisible scar beneath their chin', 'an aura of intense, focused energy',
            'hair that seems to defy gravity', 'a faded map tattooed on their back', 'a single, dark feather woven into their hair',
            'a habit of chewing on a piece of straw', 'a strange, unidentifiable accent', 'a look of permanent exhaustion',
            'a preference for walking barefoot', 'a quiet confidence that borders on arrogance'
        ],
    },
    "careers": {
        "Merchant": {
            "descriptions": [
                "A shrewd negotiator with an eye for profit, they have traveled far and wide to trade goods.",
                "Their wealth was built on careful planning and the ability to find a buyer for anything.",
                "A master of logistics and supply, they can procure rare and exotic items... for the right price.",
                "Known in many ports and cities, their reputation for fair (or ruthless) deals precedes them.",
                "They see the world not as a map of nations, but as a network of supply and demand.",
            ],
            "random_facts": [
                "Their last major score was selling {item} to a noble in {location}.",
                "They once lost a fortune on a shipment of {item}, a mistake they'll never repeat.",
                "They are secretly seeking a buyer for a rare, stolen {item}.",
                "Their entire business started with a single, perfectly traded {item}.",
                "They are known for having the highest quality {item} in the entire region.",
            ],
            "item": [
                'exotic spices', 'silk from a far-off land', 'enchanted knives', 'rare dwarven spirits',
                'ancient maps', 'Gnomish contraptions', 'unbreakable Elven steel', 'barrels of salted fish',
                'medicinal herbs from a remote jungle', 'a crate of antique books'
            ],
            "location": [
                'the capital city', 'a remote desert outpost', 'a bustling port town', 'the secluded Elven kingdom',
                'the Dwarven mountain citadel', 'a lawless border town', 'the Imperial Palace', 'a forgotten village'
            ]
        },
        "Hunter": {
            "descriptions": [
                "A master of the wilderness, they can track any beast and survive in the harshest environments.",
                "They live for the thrill of the chase, pitting their skills against the most dangerous creatures.",
                "Patience and a steady hand are their greatest assets, learned over years of silent stalking.",
                "They know the secrets of the wild, from the calls of birds to the tracks of unseen monsters.",
                "Whether for sustenance, sport, or safety, they are the first line of defense against encroaching beasts.",
            ],
            "random_facts": [
                "They are famous for single-handedly taking down {prey} that terrorized a village.",
                "They carry a gruesome trophy taken from {prey}.",
                "They seek vengeance against {prey} that injured a loved one.",
                "Their most challenging hunt was tracking {prey} through treacherous mountains.",
                "They have a deep, almost spiritual connection to the land after a fateful encounter with {prey}.",
            ],
            "prey": [
                'a Giant Boar', 'a Dire Wolf', 'a Wyvern', 'a territorial Griffon',
                'a pack of Shadow Cats', 'an ancient Manticore', 'a hulking Owlbear', 'a rabid Cockatrice',
                'a brood of Giant Spiders', 'a cunning Basilisk'
            ]
        },
        "Blacksmith": {
            "descriptions": [
                "The clang of hammer on anvil is the music of their life, forging tools and weapons of war.",
                "With soot on their brow and fire in their heart, they turn raw metal into works of art and function.",
                "Their strength is not just in their arms, but in their knowledge of alloys, temperatures, and enchantments.",
                "From the simplest horseshoe to the grandest sword, their work is known for its durability and quality.",
                "They are the backbone of any settlement, providing the essential metalwork that keeps society running.",
            ],
            "random_facts": [
                "Their masterwork, {item_made}, was presented to a legendary hero.",
                "They are secretly experimenting with a rare, volatile ore to forge {item_made}.",
                "A terrible accident occurred while they were first learning to make {item_made}.",
                "They dream of one day creating {item_made} that will be remembered in song and story.",
                "A rival blacksmith stole their unique design for {item_made}.",
            ],
            "item_made": [
                'a masterwork longsword', 'a ceremonial shield', 'an intricately engraved suit of plate armor',
                'a set of perfectly balanced throwing daggers', 'a warhammer that hums with power', 'a delicate silver filigree necklace',
                'an adamantine crowbar', 'a gate of unparalleled strength', 'a self-sharpening axe', 'a helmet forged in the shape of a dragon\'s head'
            ]
        },
        "Scholar": {
            "descriptions": [
                "Preferring the company of books to people, they are a repository of forgotten lore and knowledge.",
                "They believe that every problem can be solved with enough research and a well-stocked library.",
                "Their quest is for truth, seeking to uncover the secrets of the past to understand the present.",
                "Often lost in thought, their mind is a chaotic library of facts, theories, and unanswered questions.",
                "They have spent their life deciphering ancient texts and consulting with the wise (and the dead).",
            ],
            "random_facts": [
                "They are the world's foremost expert on {topic}.",
                "They were driven from their last university for their radical theories about {topic}.",
                "They are on a quest to find a lost library said to contain the ultimate truth about {topic}.",
                "A rival scholar is trying to discredit their life's work on {topic}.",
                "They once accidentally unleashed a minor magical anomaly while researching {topic}.",
            ],
            "topic": [
                'an ancient, fallen empire', 'the language of dragons', 'the nature of celestial magic',
                'the ecosystem of the Underdark', 'the genealogy of the royal family', 'the principles of golem construction',
                'the history of a great war', 'the prophecies of a forgotten seer', 'the anatomy of mythical beasts', 'the theory of planar travel'
            ]
        },
        "Guard": {
            "descriptions": [
                "A bastion of order in a chaotic world, they stand watch and keep the peace with a steady hand.",
                "They have seen the best and worst of society from their post, and it has left them jaded but resolute.",
                "Their life is one of routine and vigilance, punctuated by moments of sudden, violent action.",
                "Loyalty is their currency, and their spear and shield are the tools of their trade.",
                "They are the thin line between civilization and the lawlessness that lies just beyond the walls.",
            ],
            "random_facts": [
                "They once foiled a major conspiracy while stationed at {post_location}.",
                "They are haunted by a mistake they made that cost someone their life at {post_location}.",
                "They took this job to be close to a person of interest who frequents {post_location}.",
                "They found a strange, seemingly magical object while on duty at {post_location}.",
                "They have a reputation for being the most uncompromising guard at {post_location}.",
            ],
            "post_location": [
                "the city's main gate", "the royal treasury", "the dungeons", "the noble district",
                "the merchant's guildhall", "the docks", "a high-security prison", "the city aqueducts",
                "the Grand Temple", "a lonely watchtower"
            ]
        },
        "Adventurer": {
            "descriptions": [
                "Driven by a thirst for excitement, fame, or fortune, they delve into the dangerous, forgotten places of the world.",
                "They are a jack-of-all-trades, equally comfortable in a dungeon's shadow or a tavern's firelight.",
                "Their home is the road, and their family is the motley crew they travel with.",
                "Life for them is a series of quests, each one more dangerous and rewarding than the last.",
                "They have stared death in the face so many times it has become an old, unwelcome friend.",
            ],
            "random_facts": [
                "Their last major score was looting {item} from {location}.",
                "They are on the run after stealing {item} from a powerful figure in {location}.",
                "They seek a legendary {item} said to be hidden in {location}.",
                "They are forever changed by a harrowing experience they survived in {location} to retrieve {item}.",
                "A map tattooed on their arm is said to lead to {location}, where a priceless {item} is hidden.",
            ],
            "item": [
                'a glowing artifact', 'a bag of ancient coins', 'the eye of a cyclops', 'a dragon\'s egg',
                'a deck of magical cards', 'the Scepter of Kings', 'a soul-stealing sword', 'a potion of eternal youth',
                'a lich\'s phylactery', 'the last seed of a sacred tree'
            ],
            "location": [
                'a forgotten tomb', 'a dragon\'s lair', 'a sunken city', 'the ruins of a sky-castle',
                'a cursed forest', 'an active volcano', 'the Astral Plane', 'a goblin warlord\'s fortress',
                'a haunted crypt', 'a giant\'s treasure hoard'
            ]
        }
    }
}

class CharacterGeneratorApp:
    def __init__(self, root):
        """
        Initializes the Character Generator GUI application.
        
        Args:
            root: The root tkinter window.
        """
        self.root = root
        self.root.title("Fictional Character Generator")
        self.root.geometry("650x600")
        self.root.configure(bg="#2E2E2E")

        # --- Style Configuration ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#2E2E2E")
        style.configure("TLabel", background="#2E2E2E", foreground="#EAEAEA", font=("Segoe UI", 11))
        style.configure("TButton", background="#555555", foreground="#EAEAEA", font=("Segoe UI", 10, "bold"), borderwidth=1)
        style.map("TButton", background=[('active', '#6A6A6A')])
        style.configure("TCombobox", 
                        selectbackground="#4A4A4A", 
                        fieldbackground="#4A4A4A", 
                        background="#4A4A4A",
                        foreground="#EAEAEA",
                        arrowcolor="#EAEAEA")
        
        # --- Main Frame ---
        main_frame = ttk.Frame(root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Greeting and Instructions ---
        greeting_label = ttk.Label(
            main_frame, 
            text="Welcome to the Fictional Character Generator!",
            font=("Segoe UI", 16, "bold")
        )
        greeting_label.pack(pady=(0, 10))

        instruction_label = ttk.Label(
            main_frame,
            text="Select a career from the dropdown menu and click 'Generate' to create a new character.",
            wraplength=600
        )
        instruction_label.pack(pady=(0, 20))

        # --- Career Selection ---
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 15))

        career_label = ttk.Label(control_frame, text="Choose a Career:", font=("Segoe UI", 12))
        career_label.pack(side=tk.LEFT, padx=(0, 10))

        self.career_var = tk.StringVar()
        careers = list(CHARACTER_DATA["careers"].keys())
        self.career_dropdown = ttk.Combobox(
            control_frame, 
            textvariable=self.career_var, 
            values=careers, 
            state="readonly",
            width=20,
            font=("Segoe UI", 10)
        )
        if careers:
            self.career_dropdown.current(0)
        self.career_dropdown.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        # --- Generate Button ---
        generate_button = ttk.Button(main_frame, text="Generate Character", command=self.generate_character)
        generate_button.pack(pady=(0, 20), ipady=5)

        # --- Output Text Box ---
        self.output_text = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            font=("Courier New", 10), 
            bg="#1E1E1E", 
            fg="#D4D4D4",
            borderwidth=1,
            relief="solid",
            insertbackground="#FFFFFF" # Cursor color
        )
        self.output_text.pack(expand=True, fill="both")

    def _get_random_item(self, category, sub_category=None):
        """Helper function to get a random item from the data dictionary."""
        if sub_category:
            return random.choice(CHARACTER_DATA[category][sub_category])
        return random.choice(CHARACTER_DATA[category])
        
    def generate_character(self):
        """
        Generates a complete character sheet based on the selected career
        and displays it in the output text box.
        """
        selected_career = self.career_var.get()
        if not selected_career:
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, "Please select a career first.")
            return

        # --- Generate Core Traits ---
        first_name = self._get_random_item("names", "first_names")
        last_name = self._get_random_item("names", "last_names")
        race = self._get_random_item("physical_traits", "races")
        height = self._get_random_item("physical_traits", "heights")
        build = self._get_random_item("physical_traits", "builds")
        notable_feature = self._get_random_item("physical_traits", "notable_features")

        # --- Generate Career-Specific Details ---
        career_info = CHARACTER_DATA["careers"][selected_career]
        career_description = random.choice(career_info["descriptions"])
        
        # --- Process Random Fact Template ---
        fact_template = random.choice(career_info["random_facts"])
        
        # Find all placeholders like {placeholder}
        placeholders = re.findall(r"\{(\w+)\}", fact_template)
        
        final_fact = fact_template
        # Replace each placeholder with a random value from the corresponding list
        for placeholder in placeholders:
            if placeholder in career_info:
                # Get a copy of the list to avoid modifying the original
                possible_values = list(career_info[placeholder])
                # Ensure we don't pick the same value twice if a placeholder is repeated
                value = random.choice(possible_values)
                possible_values.remove(value)
                final_fact = final_fact.replace(f"{{{placeholder}}}", value, 1)

        # --- Format the Output String ---
        character_sheet = (
            f"CHARACTER SHEET\n"
            f"{'='*40}\n\n"
            f"{'Name:':<20} {first_name} {last_name}\n"
            f"{'Race:':<20} {race}\n"
            f"{'Height:':<20} {height}\n"
            f"{'Build:':<20} {build}\n"
            f"\n"
            f"{'Career:':<20} {selected_career}\n"
            f"{'Description:':<20} {career_description}\n"
            f"\n"
            f"{'Notable Feature:':<20} They have {notable_feature}.\n"
            f"{'Interesting Fact:':<20} {final_fact}\n\n"
            f"{'='*40}\n"
        )

        # --- Display the Output ---
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, character_sheet)

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterGeneratorApp(root)
    root.mainloop()