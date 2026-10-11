"""A small, text-based choose-your-own-adventure game."""


def choice(label, target=None, *, requires=None, item=None, ending=None):
    return {
        "label": label,
        "target": target,
        "requires": requires,
        "item": item,
        "ending": ending,
    }


ROOMS = {
    "courtyard": {
        "title": "The Overgrown Courtyard",
        "description": (
            "Rain falls over the ruins of Ashen Keep. Somewhere inside, a dragon "
            "guards the Sunheart, the only light left in the kingdom."
        ),
        "choices": [
            choice("Enter the keep", "great_hall"),
            choice("Turn back and leave", ending="lose"),
        ],
    },
    "great_hall": {
        "title": "The Great Hall",
        "description": (
            "Dusty banners hang above a cracked stone floor. Doors lead to the "
            "library, armory, garden, and a dark stairway down."
        ),
        "choices": [
            choice("Visit the library", "library"),
            choice("Visit the armory", "armory"),
            choice("Step into the garden", "garden"),
            choice("Descend to the cellar", "cellar"),
            choice("Return to the courtyard", "courtyard"),
        ],
    },
    "library": {
        "title": "The Silent Library",
        "description": (
            "Moldy books lean together on sagging shelves. A brass key glints "
            "inside an old atlas."
        ),
        "choices": [
            choice("Take the brass key", "library", item="brass key"),
            choice("Return to the great hall", "great_hall"),
        ],
    },
    "armory": {
        "title": "The Abandoned Armory",
        "description": (
            "Most of the weapons have rusted away. A usable sword and a sturdy "
            "torch remain on a workbench."
        ),
        "choices": [
            choice("Take the sword", "armory", item="sword"),
            choice("Take the torch", "armory", item="torch"),
            choice("Return to the great hall", "great_hall"),
        ],
    },
    "garden": {
        "title": "The Moonlit Garden",
        "description": (
            "A silver-leaved plant grows beneath a broken fountain. Its charm "
            "may be worth more than a weapon to a creature of magic."
        ),
        "choices": [
            choice("Take the silver charm", "garden", item="silver charm"),
            choice("Return to the great hall", "great_hall"),
        ],
    },
    "cellar": {
        "title": "The Cellar",
        "description": (
            "Cold steps descend into darkness. Without a torch, you cannot "
            "safely find your way."
        ),
        "choices": [
            choice(
                "Explore the passage by torchlight",
                "crypt",
                requires="torch",
            ),
            choice("Climb back to the great hall", "great_hall"),
        ],
    },
    "crypt": {
        "title": "The Sunken Crypt",
        "description": (
            "Your torch reveals an ancient stone door and a moonstone resting "
            "on a pedestal. The air hums with old magic."
        ),
        "choices": [
            choice("Take the moonstone", "crypt", item="moonstone"),
            choice(
                "Unlock the ancient door",
                "observatory",
                requires="brass key",
            ),
            choice("Return to the cellar", "cellar"),
        ],
    },
    "observatory": {
        "title": "The Broken Observatory",
        "description": (
            "A star map covers the domed ceiling. An empty socket sits in the "
            "center of the map; the moonstone might fit."
        ),
        "choices": [
            choice(
                "Place the moonstone in the star map",
                "dragon_lair",
                requires="moonstone",
            ),
            choice("Return to the crypt", "crypt"),
        ],
    },
    "dragon_lair": {
        "title": "The Dragon's Lair",
        "description": (
            "A vast red dragon curls around the glowing Sunheart. It opens one "
            "golden eye as you enter."
        ),
        "choices": [
            choice(
                "Challenge the dragon with your sword",
                requires="sword",
                ending="win",
            ),
            choice(
                "Offer the silver charm and ask for peace",
                requires="silver charm",
                ending="win",
            ),
            choice("Run for the exit", ending="lose"),
        ],
    },
}


def show_inventory(inventory):
    if inventory:
        print("Inventory: " + ", ".join(sorted(inventory)))
    else:
        print("Inventory: empty")


def play_game():
    inventory = set()
    room_name = "courtyard"

    print("\n=== THE SUNHEART OF ASHEN KEEP ===")
    print("Find the Sunheart and survive. Enter a choice number, or type I to")
    print("check your inventory. You can type Q at any prompt to quit.\n")

    while True:
        room = ROOMS[room_name]
        print(f"\n--- {room['title']} ---")
        print(room["description"])

        while True:
            available = [
                option
                for option in room["choices"]
                if not option["item"] or option["item"] not in inventory
            ]
            print()
            for number, option in enumerate(available, start=1):
                label = option["label"]
                if option["requires"] and option["requires"] not in inventory:
                    label += f" [requires {option['requires']}]"
                print(f"{number}. {label}")

            answer = input("\nYour choice: ").strip().lower()
            if answer == "i":
                show_inventory(inventory)
                continue
            if answer == "q":
                print("\nYou leave the adventure unfinished.")
                return False
            if not answer.isdigit() or not 1 <= int(answer) <= len(available):
                print("Please enter one of the listed numbers, I, or Q.")
                continue

            selected = available[int(answer) - 1]
            required = selected["requires"]
            if required and required not in inventory:
                print(f"You can't do that yet; you need the {required}.")
                continue

            item = selected["item"]
            if item:
                inventory.add(item)
                print(f"You added the {item} to your inventory.")
                continue

            if selected["ending"] == "win":
                print(
                    "\nThe dragon lowers its head. Whether by courage or "
                    "kindness, you claim the Sunheart and escape the keep. "
                    "The kingdom's lights blaze back to life. You win!"
                )
                return True
            if selected["ending"] == "lose":
                print(
                    "\nYou turn away from the danger, but the keep's darkness "
                    "swallows your chance to save the kingdom. Game over."
                )
                return False

            room_name = selected["target"]
            break


def main():
    while True:
        play_game()
        try:
            again = input("\nPlay again? (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nThanks for playing!")
