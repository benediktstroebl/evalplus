Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary and sum its digits
    :return: String of binary number of the sum of digits of n
    """
    total_sum = 0
    n = str(n)
    for digit in n:
        total_sum += int(digit)
    return bin(total_sum).replace('0b', '')
```

The function `solve` takes an integer `n` as its argument and returns a string of the binary representation of the sum of its digits. The function converts the integer to a string, loops through each digit of the number, and adds its value to the `total_sum` variable. After collecting the sum of the digits, the function converts the `total_sum` to a binary string by using the `bin` function and replaces the '0b' prefix with an empty string using the `replace` method. 

This problem can be solved using a variety of concepts related to Python strings, integers, and loops. Although the use of the `bin` function may be misleading as it converts the value to a binary string, the value of `total_sum` was not actually represented in binary. It is important to carefully read the provided examples and constraints when approaching problems like these. 

The function can be tested as following: 
```python
test_cases = [
    (1000, "1"),
    (150, "110"),
    (147, "1100")
]

for n, expected in test_cases:
    actual = solve(n)
    print(f"For N = {n}, expected '{expected}' but got '{actual}'")
```
Which confirms the expected output for the provided test cases.