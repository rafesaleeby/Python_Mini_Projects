# Inputs
start_miles = float(input("Starting odometer reading: "))
end_miles = float(input("Ending odometer reading: "))
gallons_pumped = float(input("Total gallons of gas pumped on the trip: "))
total_spent = float(input("Total money spent at the pump: $"))

# Calculations
distance = end_miles - start_miles
actual_mpg = distance / gallons_pumped
price_per_gallon = total_spent / gallons_pumped
cost_per_mile = total_spent / distance

# Output
print("\n--- Road Trip Cost Summary ---")
print(f"Total Distance: {distance:.1f} miles")
print(f"Actual Fuel Economy: {actual_mpg:.1f} MPG")
print(f"Average Gas Price: ${price_per_gallon:.2f}/gallon")
print(f"Cost Per Mile: ${cost_per_mile:.2f}/mile")