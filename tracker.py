# Personal Learning Tracker
# Version: 1.0
# Author: Sofiia

from datetime import datetime
print("=== Personal Learning Tracker ===")

while True:
    print("\n1. Add new learning activity")
    print("2. View all activities")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        activity = input("What did you learn today? ")

        with open("learning_log.txt", "a", encoding="utf-8") as file:
            date = datetime.now().strftime("%Y-%m-%d")
            file.write(f"{date} — {activity}\n")

        print("Saved successfully!")

    elif choice == "2":
      try:
         with open("learning_log.txt", "r", encoding="utf-8") as file:
             lines = file.readlines()
             print("\nYour learning activities:")
             for i, line in enumerate(lines, start=1):
                 print(f"{i}. {line.strip()}")
             print(f"\nTotal activities: {len(lines)}")
      except FileNotFoundError:
          print("No activities yet.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:

        print("Invalid option. Try again.")
