
# FareCalc Travel Optimizer

A Python-based fare calculation system for a ride-sharing service called **CityCab**.  
This project calculates ride fares based on distance, vehicle type, and surge pricing.

---

## Features

- Multiple vehicle types:
  - Economy
  - Premium
  - SUV

-  Distance-based fare calculation

-  Surge pricing:
  - Applied during peak hours (5 PM – 8 PM)

-  Input validation:
  - Valid vehicle type check
  - Hour validation (0–23)

-  Generates a formatted price receipt

---

##  Fare Calculation Logic

- Base Fare = Distance × Rate per km
- Surge Pricing:
  - If time is between **17–20**, fare is multiplied by **1.5**

---

##  Rates per km

| Vehicle Type | Rate (₹/km) |
|-------------|------------|
| Economy     | 10         |
| Premium     | 18         |
| SUV         | 25         |

---

