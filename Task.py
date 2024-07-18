import time

class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.is_running = False
        self.elapsed_time = 0

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.is_running:
            self.stop_time = time.time()
            self.elapsed_time += self.stop_time - self.start_time
            self.is_running = False
        else:
            print("Stopwatch is not running.")

    def reset(self):
        self.start_time = 0
        self.stop_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def elapsed(self):
        if self.is_running:
            return self.elapsed_time + (time.time() - self.start_time)
        else:
            return self.elapsed_time


def main():
    stopwatch = StopWatch()
    while True:
        print("1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Elapsed Time")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            stopwatch.start()
        elif choice == "2":
            stopwatch.stop()
        elif choice == "3":
            stopwatch.reset()
        elif choice == "4":
            print("Elapsed Time: ", round(stopwatch.elapsed(), 2), "seconds")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()