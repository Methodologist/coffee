from datetime import datetime
import time

class Coffee():
    def __init__(self, temperature=None, volume=0):
        self.temperature = temperature
        self.volume = volume

    def temp(self):
        fresh_cup = 160                               #average fresh cup of coffee temperature
        cooled_cup = 70                               
        start_time = datetime.now()
        duration_seconds = 1225
        while fresh_cup > cooled_cup:
            current_time = datetime.now()
            elapsed_time = current_time - start_time
            time_passed_percentage = min(elapsed_time.total_seconds() / duration_seconds, 1.0)
            new_value = fresh_cup - (fresh_cup - cooled_cup) * time_passed_percentage
            print(f"Current temperature: {new_value}")
            time.sleep(5)

    def fill(self):
        amount = input("Enter the amount of coffee to fil as a % 100 being max")
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Negative volume is not allowed.")
            self.volume = amount
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def empty(self):
        self.volume = 0

    def sip(self):
        self.volume *= 0.9
        return self.volume

    def gulp(self):
        self.volume *= 0.8
        return self.volume

def main():
    try:
        coffee = Coffee()  # Create an instance of Coffee
        coffee.fill()
        coffee.temp()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
