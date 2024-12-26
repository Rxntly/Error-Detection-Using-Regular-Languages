## This code checks for  **ODD PARITY**

def parityCheck(string):

    message = string[:-1]  # remove parity bit
    parityBit = string[-1]  # store parity bit

    count = 0

    # Check number of 1s
    for bit in message:
        if bit == '1':
            count += 1

    # Determine expected parity 
    if count % 2 == 0:
        parity = '1'
    else:
        parity = '0'

    # Match with parity bit
    if parityBit == parity:
        return "Good Integrity"
    else:
        return "Bad Integrity"
    

# Test Bench
testBench = [
    "1010100",  # (Correct)
    "0000000",  # (False)
    "11111011", # (Correct)
    "1101001",  # (False)
    "011",      # (False)
    "0000001",  # (Correct)
    "1111001",  # (Correct)
    "111111",   # (False)
    "1000011",  # (Correct)
    "110",      # (False)
]

def showTestCases():
    for test in testBench:
        # Purely to make output a little more readable
        prettyOutput = ""
        printAfter = 20
        for x in range(abs(printAfter - len(test))):
            prettyOutput += "-" 
        # Prints output
        print(f"Input: {test} {prettyOutput}> {parityCheck(test)}")


def main():
    while True:
        print("\nChoose an option:")
        print("1. Enter your own input")
        print("2. See pre-existing test cases")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            while True:
                user_input = input("Enter a binary string (with parity bit): ")
                # Check if the input is a valid binary string
                if all(bit in '01' for bit in user_input):
                    print(f"Input: {user_input} > {parityCheck(user_input)}")
                    
                    # Ask if they want to make another guess
                    another_guess = input("Would you like to enter another binary string? (y/n): ").lower()
                    if another_guess != 'y':
                        break 
                else:
                    print("Invalid input! Please enter a binary string (only '0' and '1').")
        
        elif choice == '2':
            showTestCases()
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

# Run code
if __name__ == "__main__":
    main()
