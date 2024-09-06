Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    temp_n = str(n)
    while temp_n:
        digit = temp_n[-1]
        total_sum += int(digit)
        temp_n = temp_n[:-1]
    return format(total_sum, 'b')
```

This function takes an integer `n` as its parameter and uses a while loop to iterate through its digits. It converts the integer to a string to easily slice off the last digit and accumulate the sum of digits in binary form. The sum is then returned as a string.

The code is encapsulated in a function and does not rely on any external variables or functions, making it self-contained and easy to test and use in other scripts.