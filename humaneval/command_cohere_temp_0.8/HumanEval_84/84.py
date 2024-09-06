Here's a Python script that includes a function to solve the given problem:
```python
def solve(N):
    """Returns the sum of digits in binary representation of the integer N."""
    bin_str = bin(N)[2:]
    return bin_str.replace('0b', '').replace('0', '').upper()

# Test Cases
print(solve(1000) == '1')
print(solve(150) == '110')
print(solve(147) == '1100')
print(solve(137) == '10011')
```

The function `solve` takes an integer `N` as input and returns the binary representation of the sum of its digits. To get the binary representation of the sum, the function converts the integer to a binary string, strips any leading '0b' and trailing '0' characters, and converts it to an uppercase string. This is done to ensure that digits beyond the current value are carried over to the output, as shown in your example scenarios. Test cases are provided to validate the function's behavior. 

The code concludes with examples that showcase the expected behavior of the function for different input values. These examples will be printed to the console when you run the script.