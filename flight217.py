import time
import random

def slow_print(text, delay=0.03):  # lowered default slightly - 0.05 feels laggy
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ====================== GAME DATA ======================
morality = 50
honor = 50
wife_alive = True
terror_alert = 0
sabrina_emotion = 50

# ====================== CORE FUNCTIONS ======================
def show_stats():
    print("\n" + "-" * 50)
    print(f"Morality: {morality} | Honor: {honor} | Terror Alert: {terror_alert}")
    print("Sabrina: " + ("ALIVE ❤️" if wife_alive else "DECEASED 💔"))
    print("-" * 50)

def talk_choice(context: str) -> int:
    """One flexible conversation function. Pass context for unique flavor."""
    print("\n" + "=" * 40)
    print(f"What do you say to Sabrina? ({context})")
    print("[1] Optimistic / future-focused")
    print("[2] Caring / check on her")
    print("[3] Baby-focused")
    print("=" * 40)
    
    choice = input("Your choice: ").strip()
    
    if choice == "1":
        slow_print("\nSabrina responds warmly to your optimism.")
        return 15
    elif choice == "2":
        slow_print("\nShe appreciates you noticing how she feels.")
        return 10
    elif choice == "3":
        slow_print("\nHer eyes light up talking about the baby.")
        return 20
    else:
        slow_print("\nAwkward response. She laughs it off.")
        return 5

# ====================== SCENES ======================
def pre_hijack_conversations():
    global sabrina_emotion
    
    slow_print("\n[Seat 14A-14B - 30,000 feet]")
    slow_print("You are Jake. Sabrina rests her hand on her belly.")
    
    scenes = [
        "Smooth flight, talking about the future",
        "Flight attendant offers champagne (she declines)",
        "Turbulence hits",
        "Naming the baby"
    ]
    
    for scene in scenes:
        slow_print(f"\n--- {scene} ---")
        sabrina_emotion += talk_choice(scene)
        time.sleep(0.8)
    
    # Final emotion readout
    if sabrina_emotion >= 80:
        slow_print("\n❤️ Sabrina is radiant. She kisses you deeply.")
    elif sabrina_emotion >= 60:
        slow_print("\n💛 She's content and close.")
    else:
        slow_print("\n💔 Tension lingers between you.")

def first_hijack_choice():
    global morality, honor, wife_alive, terror_alert
    
    slow_print("\n[20 MINUTES AFTER HIJACK]")
    slow_print("Two armed terrorists walk the aisle checking passports.")
    slow_print("One stops at your row. 'You. Stand up.'")
    
    while True:
        print("\n" + "=" * 45)
        print("What do you do?")
        print("[1] ATTACK")
        print("[2] NEGOTIATE")
        print("[3] HIDE / comply")
        print("=" * 45)
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            slow_print("\nYou lunge for his weapon...")
            terror_alert += 45
            morality -= 25
            
            if random.random() < 0.65:  # higher chance of tragedy
                slow_print("Bullets fly. Sabrina is hit.")
                wife_alive = False
            else:
                slow_print("You get shot but shield her.")
                morality -= 15
            break
            
        elif choice == "2":
            slow_print("\nYou plead for your pregnant wife.")
            if morality >= 35:
                slow_print("They separate her to the back. She's alive... for now.")
                honor += 15
                terror_alert += 15
            else:
                slow_print("They don't believe you. Brutal rifle butt to your face.")
                terror_alert += 10
            break
            
        elif choice == "3":
            slow_print("\nYou freeze and look away.")
            honor -= 25
            morality -= 10
            terror_alert += 8
            if terror_alert > 50 and random.random() < 0.6:
                wife_alive = False
            break
            
        else:
            slow_print("Invalid choice.")

def determine_ending():
    slow_print("\n" + "🔻" * 30)
    if not wife_alive:
        ending_suicide()
    elif morality <= 25:
        ending_hero_tragedy()
    elif terror_alert >= 70:
        ending_cold_case()  # or new bad ending
    else:
        # Add more nuanced endings later
        ending_cold_case()

# ====================== ENDINGS ======================
def ending_suicide():
    slow_print("         ENDING: HER VOICE, THEN SILENCE")
    # ... (keep your good version)

def ending_hero_tragedy():
    slow_print("         ENDING: SAVED WIFE, LOST SOUL")
    # ...

def ending_cold_case():
    slow_print("              ENDING: COLD CASE")
    # ...

# ====================== MAIN ======================
def print_menu():
    # ... keep yours, it's fine

def how_to_play():
    # ... keep or improve

def start_game():
    global morality, honor, wife_alive, terror_alert, sabrina_emotion
    # Reset everything
    morality = honor = 50
    wife_alive = True
    terror_alert = 0
    sabrina_emotion = 50
    
    slow_print("\n[SYSTEM] Flight 217 protocols engaged...")
    pre_hijack_conversations()
    
    slow_print("\n" + "!" * 60)
    slow_print("              TERRORISTS HAVE CONTROL")
    slow_print("!" * 60)
    
    first_hijack_choice()
    show_stats()
    determine_ending()
    
    slow_print("\nThank you for playing Flight 217.")

# ====================== RUN ======================
if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            start_game()
            break
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            slow_print("\nDisconnecting...")
            break
        else:
            slow_print("\n[ERROR] Invalid choice.")