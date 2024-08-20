def print_card(prompt):
    border = '+' + '-' * (len(prompt) + 2) + '+'
    print(border)
    print(f'| {prompt} |')
    print(border)

def ask(number):
    while True:
        prompt = f"Is the number bigger than {number}? (y/n)"
        print_card(prompt)
        answer = input().strip().lower()
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
    print_card(f"The number you thought of is {low}.")

find_number()
