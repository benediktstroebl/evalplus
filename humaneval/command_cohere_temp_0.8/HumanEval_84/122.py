Here's a Python script that contains a function which computes the sum of digits of an integer in binary:
```python
def solve(N):
    # Convert the integer to a string
    N_str = str(N)
    
    # Initialize the sum of digits in binary to an empty string
    result = ''
    
    # Loop through each digit in the integer
    for digit in N_str:
        # Convert the digit to a binary string
        digit_bin = bin(int(digit))[2:]
        
        # Append the binary representation of the digit to the result
        result += digit_bin
    
    # Return the result
    return result
```

The binary representation of the digits is obtained by converting each digit to binary using `bin()`, and then slicing the result starting from the third character (`[2:]`), which gives the binary representation without the '0b' prefix. Finally, the binary representations of all the digits are concatenated together to form the output.