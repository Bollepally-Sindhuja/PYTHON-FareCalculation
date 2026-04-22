def calculate_fare(km, vehicle_type, hour):
    rates = {
        'ECONOMY': 10,
        'PREMIUM': 18,
        'SUV': 25
    }
    if vehicle_type not in rates:
        return "Service Not Available"
    
    base_rate = rates[vehicle_type]
    total = km * base_rate
    if hour >= 17 and hour <= 20:
        total *= 1.5   
    return total
try:
    print("----- CityCab Fare Calculator -----") 
    km = float(input("Enter distance (in km): "))
    vehicle_type = input("Enter vehicle type (Economy/Premium/SUV): ").strip().upper()
    while True:
        hour = int(input("Enter hour of travel (0-23): "))
        if hour>=0 and hour <= 23:
            break
        else:
            print("Invalid hour! Please enter between 0 and 23.")
    
    result = calculate_fare(km, vehicle_type, hour)
    
    print("\n----- Price Receipt -----")
    
    if result == "Service Not Available":
        print("Vehicle Type:", vehicle_type)
        print("Status: Service Not Available")
    else:
        print(f"Distance: {km} km")
        print(f"Vehicle Type: {vehicle_type}")
        print(f"Travel Hour: {hour}")
        
        if hour>=17 and hour <= 20:
            print("Surge Pricing Applied: YES (1.5x)")
        else:
            print("Surge Pricing Applied: NO")
        
        print(f"Total Fare: ₹{result:.2f}")
except ValueError:
    print("Invalid input! Please enter correct numeric values.")