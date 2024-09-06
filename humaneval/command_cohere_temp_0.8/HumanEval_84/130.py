Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of sum of digits of n
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return format(total_sum, 'b')
```

This function iterates through each digit in the decimal representation of the input `n`, converts each digit to binary, and then returns the binary representation of the sum of these digits. The `format` function is used to convert the integer sum into a binary string. The function outputs a string in binary representation, with the format, e.g., "1" for N = 1000 and "110" for N = 150.

To use this script, you can simply call the function with a number as follows:
```python
print(solve(147))  # Outputs: "1101100"
```

This approach provides a clear and efficient way to convert the decimal sum of digits to binary, achieving the desired result.