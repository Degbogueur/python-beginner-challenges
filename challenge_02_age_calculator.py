from datetime import datetime

birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
print(f"You are approximately {current_year - birth_year} years old.")