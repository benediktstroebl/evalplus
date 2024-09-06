Here's a Python script that contains a function which computes the sum of digits of a given integer `N` in binary, as requested:
```python
def solve(N):
    # Convert the integer to a binary string
    bin_str = bin(N)[2:]
    
    # Initialize the sum of digits to 0
    sum_digits = 0
    
    # Loop through each digit in the binary representation
    for digit in bin_str:
        # Convert the digit to an integer (remove leading zeros)
        digit_int = int(digit)
        sum_digits += digit_int
    
    return format(sum_digits, 'b')

# Test cases
print(solve(1000))  # Should output: 1
print(solve(150))   # Should output: 110
print(solve(147))   # Should output: 1100
```

This code defines a function `solve` that takes an integer `N` as input and returns the binary string representation of the sum of its digits. The function first converts the integer to a binary string and then iterates over each digit, converting it to an integer and adding it to the `sum_digits` variable. Finally, it returns the binary string representation of `sum_digits`.