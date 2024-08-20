def ask(number):
    while True:
        answer = input(f"Is the number bigger than {number}? (y/n): ").strip().lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print("Please enter 'y' or 'n'.")

def find_number():
    low = 1
    high = 2
    while True:
        response = ask(high)
        if response == 'y':
            break
        else:
            low = high
            high *= 2

    while low <= high:
        mid = (low + high) // 2
        response = ask(mid)
        
        if response == 'y':
            low = mid + 1
        elif response == 'n':
            high = mid - 1
    
    print(f"The number you thought of is {high + 1}.")

find_number()
