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
Random_Encounters = {
    "generic": {
        "time_of_day": [
            "At the crack of dawn", "In the bright morning sun", "At high noon",
            "In the late afternoon", "As the sun begins to set", "At dusk",
            "In the dead of night", "Under a full moon"
        ],
        "weather": [
            "with a clear, blue sky overhead.", "with fluffy white clouds drifting by.", "under a hazy, humid sun.",
            "as a light, drizzling rain begins to fall.", "in a sudden, heavy downpour.",
            "as a thick, mysterious fog rolls in.", "with a strong, chilling wind blowing against them.",
            "under an ominous, overcast sky."
        ],
        "complications_or_twists": [
            "It's an ambush by bandits.", "The person or object is not what it seems.", "A powerful monster is drawn to the scene.",
            "The encounter is a distraction for a thief in your party.", "There is a valuable reward for helping.",
            "Getting involved will make a powerful enemy.", "This is a case of mistaken identity.",
            "A sudden change in weather makes things much worse.", "The situation is a test from a hidden deity."
        ]
    },
    "Wilderness": {
        "core_encounter": [
            "You come across {subject} blocking the forest path.",
            "You find a seemingly abandoned {subject} in the middle of a clearing.",
            "The path ahead leads through {location}, which is rumored to be haunted.",
            "You hear the sounds of a struggle coming from {location} and discover {subject}."
        ],
        "subjects": [
            "an overturned merchant's cart, its goods scattered", "a lone, weeping child", "a strangely friendly goblin",
            "a mysterious, hooded figure studying a tree", "a dying messenger's horse", "a group of cheerful pilgrims",
            "a territorial beast guarding its kill", "a hermit's secluded hut"
        ],
        "locations": [
            "a decrepit, ancient bridge", "a small, overgrown ruin", "a dark, foreboding copse of trees",
            "a shallow, babbling brook", "a crossroads with a weathered signpost", "the shadow of a great cliff"
        ]
    },
    "Mountains": {
        "core_encounter": [
            "The narrow mountain pass is blocked by {subject}.",
            "You spot {subject} perilously close to the edge of {location}.",
            "A rockslide has revealed the entrance to {location}, from which you see {subject} emerge.",
            "You discover a freshly made campsite near {location}, but it's empty except for {subject}."
        ],
        "subjects": [
            "a pair of bickering dwarves arguing over a map", "a majestic Griffon tending to its nest", "an avalanche survivor",
            "a prospector who has struck a rich vein of ore", "a broken wagon from a failed expedition", "a reclusive giant"
        ],
        "locations": [
            "a treacherous, icy ledge", "a forgotten dwarven outpost", "a high-altitude cave network",
            "a rope bridge swaying violently in the wind", "a frozen waterfall"
        ]
    },
    "City": {
        "core_encounter": [
            "A commotion in {location} draws your attention to {subject}.",
            "In a dark alleyway, you witness {subject} being cornered by thugs.",
            "You are approached by {subject}, who offers a quest with a suspicious reward.",
            "The city guard has cordoned off {location} because of {subject}."
        ],
        "subjects": [
            "a charlatan selling fake miracle potions", "a street urchin with something valuable they stole", "a corrupt city guard demanding a 'toll'",
            "a public crier announcing a royal decree", "a noble's runaway pet", "a clandestine meeting between spies"
        ],
        "locations": [
            "the bustling marketplace", "the city sewers", "a high-end tavern", "the shadow of the gallows", "a grand temple's steps"
        ]
    },
    "Near Water": {
        "core_encounter": [
            "Washed ashore near {location}, you find {subject}.",
            "A boat carrying {subject} is in distress in the middle of the river.",
            "You see {subject} emerging from the water at {location}.",
            "Fishing at {location}, you unexpectedly hook onto {subject}."
        ],
        "subjects": [
            "a treasure chest tangled in seaweed", "a shipwreck survivor", "a message in a bottle",
            "a group of pirates burying their loot", "a mermaid or river spirit", "a giant crab blocking the beach"
        ],
        "locations": [
            "a rocky shoreline", "a misty lake", "the banks of a wide, flowing river", "a hidden cove", "a decaying dock"
        ]
    }
}
LOOT_DATA = {
    # Each key is the "value" of the items within.
    "1": {
        "description": "Worthless Trinkets",
        "items": [
            "A chipped clay marble", "A rusty, bent nail", "A single, worn-out boot", "A button made of common wood",
            "A small, smooth river stone", "A piece of lint", "A frayed bit of rope, about 6 inches long",
            "A chicken feather", "A single, dull copper piece, minted in a forgotten kingdom",
            "A shard of a broken clay pot", "A pet rock with a crudely painted face", "A dried-up leaf of a common tree",
            "A cracked bottle cap", "A tooth from a small animal (likely a squirrel)", "A single, unmated sock",
            "A dead insect in a small jar", "A small clump of dirt", "A piece of charcoal",
            "The stub of a used candle", "A tarnished brass button"
        ]
    },
    "2": {
        "description": "Common Items",
        "items": [
            "A simple wool blanket", "A set of bone dice", "A waterskin, half-full of stale water", "A small pouch of salt",
            "A whetstone for sharpening blades", "50 feet of hempen rope", "A small, sharp knife", "A tin spoon",
            "A bar of unscented soap", "A half-empty ink pot", "A small mirror of polished steel",
            "A tinderbox with flint and steel", "A wooden comb", "A small sack of dried beans",
            "A leather belt pouch", "A handful of torches", "A block of cheese, slightly moldy",
            "A spool of thick, black thread", "A set of peasant's clothes", "A half-burnt-down candle"
        ]
    },
    "3": {
        "description": "Uncommon Goods",
        "items": [
            "A bottle of cheap wine", "A silver piece", "A beautifully crafted leather bookmark",
            "A small pouch of aromatic spices", "A map of the local region, slightly inaccurate",
            "A potion of minor healing (heals 1d4 health)", "A magnifying glass", "A set of loaded dice",
            "A steel helmet", "A quiver containing 10 iron-tipped arrows", "A healer's kit with 3 uses",
            "A silver-plated holy symbol", "A spyglass", "A well-made shortsword",
            "A small pot of good-quality ink", "A beautifully illustrated playing card (the Ace of Spades)",
            "A bag of 20 ball bearings", "A small hunting trap", "A traveler's cloak with many pockets",
            "A necklace of polished animal teeth"
        ]
    },
    "4": {
        "description": "Valuable Wares",
        "items": [
            "A gold piece", "A pouch containing 10 silver pieces", "A finely woven silk handkerchief",
            "A small gemstone (e.g., a quartz or agate)", "A heavy crossbow", "A chain shirt",
            "A bottle of fine elven wine", "A silver dagger", "A set of cartographer's tools",
            "A musical instrument (e.g., a lute or flute)", "A scroll with a single, simple spell (e.g., Light)",
            "A large steel shield with a simple emblem", "A Potion of Growth (makes you larger for 1 hour)",
            "A bag of caltrops", "A well-made leather backpack", "A set of thieves' tools",
            "A silver ring with a small, inset stone", "A pair of sturdy leather boots",
            "A writ of passage for a nearby city", "A small block of high-quality incense"
        ]
    },
    "5": {
        "description": "Minor Magical Items",
        "items": [
            "A Potion of Greater Healing (heals 2d4+2 health)", "A +1 arrow (a single magical arrow)",
            "A cloak that billows dramatically on command", "Ever-smoking bottle (uncorks to produce thick smoke)",
            "A talking doll that only says 'Mama!'", "A small, unbreakable orb", "A rope that ties and unties itself on command",
            "A mug that keeps any liquid inside it pleasantly warm", "A self-inking quill",
            "A hat that can change its color three times a day", "A stone that whispers compliments",
            "A pair of boots that always make you walk in step with music", "A coin that always lands on its edge",
            "A wineskin that turns water into very cheap, sour wine", "A compass that points to the nearest tavern",
            "A small bag of never-ending hard candy", "A bedroll that is always perfectly dry and comfortable",
            "A small bell that makes no sound when rung", "A set of spectacles that make the wearer look more intelligent",
            "A single glove that can clean any surface it wipes"
        ]
    },
    "6": {
        "description": "Quality Gear & Gems",
        "items": [
            "A beautifully balanced longsword", "A suit of studded leather armor", "A large, flawless amethyst gemstone",
            "A heavy gold necklace", "A deed to a small, insignificant plot of land", "A masterwork shield",
            "A fine horse with saddle and bridle", "A Potion of Invisibility (lasts 1 hour)",
            "A spell scroll of a 2nd level spell (e.g., 'Misty Step')", "A set of five +1 crossbow bolts",
            "A pouch of 25 gold pieces", "A platinum piece", "An ornate, silver-inlaid music box",
            "A spyglass of Gnomish design with x20 magnification", "A ring of feather falling",
            "A bag of holding (holds 250 lbs)", "A masterwork suit of smith's tools",
            "A map purported to lead to a minor treasure", "A letter of recommendation from a minor noble",
            "A set of dice carved from dragon bone"
        ]
    },
    "7": {
        "description": "Potent Magical Items",
        "items": [
            "A +1 weapon (longsword, dagger, etc.)", "A +1 shield", "A wand of magic missiles (7 charges)",
            "Boots of elvenkind (wearer makes no sound when moving)", "A helm of comprehending languages",
            "A cloak of protection +1", "Gauntlets of ogre power (sets Strength to 19)",
            "A Potion of Flying (lasts 1 hour)", "A gem of seeing (3 charges)", "A pearl of power",
            "Bracers of archery (+2 to ranged attack damage)", "A hat of disguise", "A pipe of smoke monsters",
            "An immovable rod", "A lantern of revealing", "A phylactery of faithfulness",
            "A sending stone (one of a pair)", "A driftglobe that follows you and sheds light",
            "A robe of useful items", "A decanter of endless water"
        ]
    },
    "8": {
        "description": "Rare & Powerful Items",
        "items": [
            "A suit of +1 chain mail", "A flame tongue sword", "A staff of healing", "Boots of speed",
            "A ring of the ram", "A folding boat", "A portable hole", "A necklace of fireballs",

            "A bag of beans", "A spell scroll of a 4th level spell (e.g., 'Dimension Door')",
            "A small chest containing 100 platinum pieces", "A deed to a well-known tavern in a major city",
            "A +2 weapon", "A manual of golem creation (clay)", "A horn of blasting", "A cloak of the bat",
            "A dimensional shackes", "A cubic gate", "An amulet of health", "A belt of dwarvenkind"
        ]
    },
    "9": {
        "description": "Very Rare & Wondrous Items",
        "items": [
            "A suit of +2 plate armor", "A sword of sharpness", "A staff of fire", "A carpet of flying",
            "A magic spyglass that can see through walls", "A horn of Valhalla (silver)",
            "An amulet of the planes", "A +3 shield", "A belt of giant strength (frost/stone)",
            "A spellguard shield", "A cloak of invisibility", "A ring of regeneration",
            "A rod of absorption", "A tome of understanding", "A manual of quickness of action",
            "A dancing sword", "A giant slayer axe", "A vorpal sword (on a nat 20, decapitates)",
            "A sphere of annihilation", "A staff of power"
        ]
    },
    "10": {
        "description": "Legendary Artifacts",
        "items": [
            "A Holy Avenger sword", "A Luck Blade (1 wish)", "The Deck of Many Things", "A Defender sword",
            "The Vorpal Sword", "A Staff of the Magi", "A Ring of Three Wishes",
            "The Robe of the Archmagi", "A suit of +3 plate armor", "A Belt of Storm Giant Strength (sets Strength to 29)",
            "The Sphere of Annihilation", "An Apparatus of the Crab", "The Talisman of Pure Good",
            "The Talisman of Ultimate Evil", "The Book of Exalted Deeds", "The Book of Vile Darkness",
            "A Cloak of Invisibility", "The Ioun Stone of Mastery", "The Scarab of Protection",
            "The Well of Many Worlds", "A sovereign glue"
        ]
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
        self.root.title("Fictional Content Generator")
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
            text="Welcome to the Fictional Content Generator!",
            font=("Segoe UI", 16, "bold")
        )
        greeting_label.pack(pady=(0, 10))

        # --- Author Name ---
        author_label = ttk.Label(
            main_frame,
            text="by ScryingOwlbear",
            font=("Segoe UI", 11, "italic"),
            foreground="#AAAAAA"
        )
        author_label.pack(pady=(0, 20))

        instruction_label = ttk.Label(
            main_frame,
            text="Select an option from a dropdown and click its 'Generate' button to create content.",
            wraplength=600
        )
        instruction_label.pack(pady=(0, 30))

        # --- Career Generator Row ---
        career_frame = ttk.Frame(main_frame)
        career_frame.pack(fill=tk.X, pady=(0, 10))

        career_label = ttk.Label(career_frame, text="Choose a Career:", font=("Segoe UI", 12))
        career_label.pack(side=tk.LEFT, padx=(0, 10))

        self.career_var = tk.StringVar()
        careers = list(CHARACTER_DATA["careers"].keys())
        self.career_dropdown = ttk.Combobox(
            career_frame, 
            textvariable=self.career_var, 
            values=careers, 
            state="readonly",
            width=20,
            font=("Segoe UI", 10)
        )
        if careers:
            self.career_dropdown.current(0)
        self.career_dropdown.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        generate_char_button = ttk.Button(career_frame, text="Generate Character", command=self.generate_character)
        generate_char_button.pack(side=tk.LEFT, padx=(10, 0))

        # --- Environment Generator Row ---
        env_frame = ttk.Frame(main_frame)
        env_frame.pack(fill=tk.X, pady=10)

        env_label = ttk.Label(env_frame, text="Choose an Environment:", font=("Segoe UI", 12))
        env_label.pack(side=tk.LEFT, padx=(0, 10))

        self.environment_var = tk.StringVar()
        environments = [key for key in Random_Encounters.keys() if key != 'generic']
        self.environment_dropdown = ttk.Combobox(
            env_frame,
            textvariable=self.environment_var,
            values=environments,
            state="readonly",
            width=20,
            font=("Segoe UI", 10)
        )
        if environments:
            self.environment_dropdown.current(0)
        self.environment_dropdown.pack(side=tk.LEFT, expand=True, fill=tk.X)

        generate_encounter_button = ttk.Button(env_frame, text="Generate Encounter", command=self.generate_encounter)
        generate_encounter_button.pack(side=tk.LEFT, padx=(10, 0))

        # --- Loot Generator Row ---
        loot_frame = ttk.Frame(main_frame)
        loot_frame.pack(fill=tk.X, pady=(10, 20))

        loot_label = ttk.Label(loot_frame, text="Choose a Loot Range:", font=("Segoe UI", 12))
        loot_label.pack(side=tk.LEFT, padx=(0, 10))

        self.loot_range_var = tk.StringVar()
        self.loot_tier_map = {f"{level}: {details['description']}": level for level, details in LOOT_DATA.items()}
        loot_ranges = list(self.loot_tier_map.keys())
        
        self.loot_dropdown = ttk.Combobox(
            loot_frame,
            textvariable=self.loot_range_var,
            values=loot_ranges,
            state="readonly",
            width=25,
            font=("Segoe UI", 10)
        )
        if loot_ranges:
            self.loot_dropdown.current(0)
        self.loot_dropdown.pack(side=tk.LEFT, expand=True, fill=tk.X)

        generate_loot_button = ttk.Button(loot_frame, text="Generate Loot", command=self.generate_loot)
        generate_loot_button.pack(side=tk.LEFT, padx=(10, 0))

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

    def generate_encounter(self):
        """
        Generates a random road encounter based on the selected environment and displays it in the output text box.
        """
        selected_environment = self.environment_var.get()
        if not selected_environment:
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, "Please select an environment first.")
            return

        # 1. Get the specific data for the selected environment
        env_data = Random_Encounters [selected_environment]
        # Also get the generic data that applies to all environments
        generic_data = Random_Encounters ["generic"]

        # 2. Pick random elements from generic and environment-specific lists
        time = random.choice(generic_data["time_of_day"])
        weather = random.choice(generic_data["weather"])
        twist = random.choice(generic_data["complications_or_twists"])
        
        # Pick from the environment-specific list
        core_template = random.choice(env_data["core_encounter"])

        # 3. Process the placeholders in the core encounter template
        final_encounter_text = core_template
        placeholders = re.findall(r"\{(\w+)\}", final_encounter_text)

        for placeholder in placeholders:
            lookup_key = placeholder + 's'
            if lookup_key in env_data:
                value = random.choice(env_data[lookup_key])
                final_encounter_text = final_encounter_text.replace(f"{{{placeholder}}}", value, 1)

        # 4. Format the final output string
        encounter_sheet = (
            f"RANDOM ENCOUNTER: {selected_environment.upper()}\n"
            f"{'='*40}\n\n"
            f"SCENE: {time}, {weather}\n\n"
            f"ENCOUNTER: {final_encounter_text}\n\n"
            f"THE TWIST: {twist}\n\n"
            f"{'='*40}\n"
        )
        # 5. Display the output
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, encounter_sheet)

    def generate_loot(self):
        """
        Generates a parcel of loot based on the selected value range.
        """
        selected_range_desc = self.loot_range_var.get()
        if not selected_range_desc:
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, "Please select a loot range first.")
            return

        # 1. Determine the target value from the user's selection
        target_value = int(self.loot_tier_map[selected_range_desc])
        
        remaining_value = target_value
        loot_parcel = []

        # 2. "Spend" the remaining value on items
        while remaining_value > 0:
            # Determine the max level of item we can afford
            max_item_level = min(remaining_value, 10) # Cannot pick an item level higher than 10
            
            # Randomly pick an item level to "buy"
            # Lower level items are more common
            possible_levels = [str(i) for i in range(1, max_item_level + 1)]
            # Give a higher chance to pick lower-value items to get more variety
            weights = [10/int(lvl) for lvl in possible_levels]
            chosen_level_str = random.choices(possible_levels, weights=weights, k=1)[0]
            chosen_level_int = int(chosen_level_str)
            
            # 3. Select an item from the chosen level
            item = random.choice(LOOT_DATA[chosen_level_str]["items"])
            loot_parcel.append(f"- (Lvl {chosen_level_str}) {item}")
            
            # 4. Decrease the remaining value
            remaining_value -= chosen_level_int
            
        # 5. Format and display the output
        loot_sheet = (
            f"LOOT PARCEL (TOTAL VALUE: {target_value})\n"
            f"{'='*40}\n\n"
        )
        loot_sheet += "\n".join(sorted(loot_parcel))
        loot_sheet += f"\n\n{'='*40}\n"

        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, loot_sheet)

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterGeneratorApp(root)
    root.mainloop()