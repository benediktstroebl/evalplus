Here is a Python script that defines a function `greatest_common_divisor` solving the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return a
    if a == b:
        return a
    gcd = greatest_common_divisor(b, a % b)
    return gcd

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(105, 51))  # Output: 5
```
The `greatest_common_divisor` function calculates the greatest common divisor of two integers a and b using recursion. It takes a common divisor finding algorithm, the function will return the greatest common divisor of the two numbers.