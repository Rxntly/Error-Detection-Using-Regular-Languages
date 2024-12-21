# Created by Raed Massoud on 12/21/2024
## This model uses **ODD PARITY**

### Main Method
def parityCheck(string):

    message = string[:-1] # remove parity bit
    parityBit = string[-1] # store parity bit

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
        return "Possible Corruption"
    
### End of Main
    
# Test Bench
testBench = [
    "1010100", # 3 1s parity bit should be 0 (Correct)
    "0000000", # 0 1s parity bit should be 1 (False)
    "11111011", # 6 1s parity bit should be 1 (Correct)
    "1101001", # 3 1s parity bit should be 0 (False)
    "011",     # 1 1  parity bit should be 0 (False)
    "0000001", # 0 1s parity bit should be 1 (Correct)
    "1111001", # 4 1s parity bit should be 1 (Correct)
    "111111"   # 5 1s parity bit should be 0 (False)
    "1000011", # 2 1s parity bit should be 1 (Correct)
    "110",     # 2 1s parity bit should be 1 (False)
]

# Run test bench
for test in testBench:

    # Purely to make out put readable / pretty
    # Please increase "print after" for string longer than 19 bits
    prettyOutput = ""
    printAfter = 20
    for x in range(abs(printAfter - len(test))):
        prettyOutput += "-" 

    # Print output
    print(f"Input: {test} {prettyOutput}> {parityCheck(test)}")
