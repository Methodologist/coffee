from datetime import datetime

class Coffee():
    def __init__(self, temperature=None, volume=0):  # Set default value for volume
        self.temperature = temperature
        self.volume = volume
        self.start_time = None  # Initialize start_time

    def start_timer(self):
        self.start_time = datetime.now()

    def get_elapsed_time(self):
        if self.start_time:
            current_time = datetime.now()
            return current_time - self.start_time
        else:
            return None

    def temp(self):
        fresh_cup = 160                         # average fresh cup of coffee temperature
        cooled_cup = 70                               
        duration_seconds = 1225

        elapsed_time = self.get_elapsed_time()
        if elapsed_time:
            time_passed_percentage = min(elapsed_time.total_seconds() / duration_seconds, 1.0)
            new_value = fresh_cup - (fresh_cup - cooled_cup) * time_passed_percentage
            print(f"Current temperature: {new_value:.2f} ferenheit")
        else:
            print("Timer hasn't started yet.")

    def fill(self):
        self.volume = 100
        self.start_timer()
        print("You fill your cup")
        
    def empty(self):
        self.volume = 0
        question = input("Would you like to fill your cup? ")
        if question.lower() == "yes":
            self.fill()
        else:
            print("You decide not to fill your cup.")

    def sip(self):
        sip_amount = 10
        if self.volume >= sip_amount:
            self.volume -= sip_amount
        else:
            self.volume -= self.volume
            print("You finish what's left with a micro-sip.")
        print(f"You take a sip, {int(self.volume)}% remains")

    def gulp(self):
        gulp_amount = 20
        if self.volume >= gulp_amount:
            self.volume -= gulp_amount
        else:
            self.volume -= self.volume
            print("You finish what's left with a sip.")
        print(f"You take a gulp, {int(self.volume)}% remains")

def main():
    coffee = Coffee()  # Create an instance of Coffee
    while True:
        if coffee.volume == 0:
            coffee.empty()
        if coffee.volume > 0:
            inquire = input("drink or check temp? ").lower()
            if "temp" or "check" in inquire:
                coffee.temp()
            if "drink" in inquire:
                drink = input("sip or gulp? ").lower()
                if "sip" in drink:
                    coffee.sip()
                if "gulp" in drink:
                    coffee.gulp()
                else:
                    print("Invalid choice. Please enter 'sip' or 'gulp'.")

if __name__ == "__main__":
    main()
