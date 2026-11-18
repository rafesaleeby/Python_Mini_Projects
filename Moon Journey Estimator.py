moon_distance_miles = 238855

speed_mph = float(input("Enter the cruising speed of your spacecraft (MPH): "))

total_hours = moon_distance_miles / speed_mph
remaining_days = int(total_hours // 24)
remaining_hours = round(total_hours % 24, 1)

print("\n---------- Moon Journey Estimator ----------")
print(f"The total distance to the moon is {moon_distance_miles}mi")
print(f"The cruising speed of your spacecraft is {speed_mph} MPH")
print(f"In total, it will take you {remaining_days} days and {remaining_hours} hours to reach the moon")