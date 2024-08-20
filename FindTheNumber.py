def ask(number):
    while True:
        answer = input(f"Is the number bigger than {number}? (y/n): ").strip().lower()
        if answer in ('y', 'n'):
            return answer
        else:
            print("Please enter 'y' or 'n'.")

def find_number():
    low = 1
    high = 2
    
    while ask(high) == 'y':
        low = high
        high *= 2

    while low <= high:
        mid = (low + high) // 2
        response = ask(mid)
        
        if response == 'y':
            low = mid + 1
        elif response == 'n':
            high = mid - 1
    
    print(f"The number you thought of is {low}.")

find_number()
