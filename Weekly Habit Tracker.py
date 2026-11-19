weekly_count = 0

for day in range(7):
    
    daily_count = 0

    print(f"\n--- Day {day + 1} ---")

    exercise_answer = input("Did you get 1 hour of exercise today? (Y/N): ").upper()
    if exercise_answer == "Y":
        daily_count = daily_count + 1
        weekly_count = weekly_count + 1
    elif exercise_answer == "N":
        pass
    else:
        print("Invalid input")
        
    reading_answer = input("Did you read for 30 minutes today? (Y/N): ").upper()
    if reading_answer == "Y":
        daily_count = daily_count + 1
        weekly_count = weekly_count + 1
    elif reading_answer == "N":
        pass
    else:
        print("Invalid input")

    studying_answer = input("Did you study for 40 minutes today? (Y/N): ").upper()
    if studying_answer == "Y":
        daily_count = daily_count + 1
        weekly_count = weekly_count + 1
    elif studying_answer == "N":
        pass
    else:
        print("Invalid input")

    print("--------------------------")
    print(f"{daily_count}/3 completed")
    print("--------------------------")


print("---------------------------------------------------------")
print(f"You completed {weekly_count} out of 21 habits this week.")
print(f"Completion rate: {(weekly_count / 21) * 100:.1f}%")
print("---------------------------------------------------------")