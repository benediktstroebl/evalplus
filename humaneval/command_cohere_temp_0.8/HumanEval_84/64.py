Here's a Python script that contains a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the sum of digits in base 2
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    binary_string = bin(total_sum)[2:]
    return binary_string
```

This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits. The function iterates through each digit in the decimal representation of `n` using a `for` loop. It converts each digit to an integer using `int(digit)` and adds it to the `total_sum` variable. After collecting the sum of the digits, the function then converts the `total_sum` to a binary string and returns it. Any leading zeros in the binary string are removed using `bin(total_sum)[2:]`.

This implementation takes an integer as input and returns a binary string that represents the sum of its digits in base 2. 
It is concise and efficient, with a time complexity of O(n), where n is the number being processed. 
This solution works for positive integers up to 10,000.