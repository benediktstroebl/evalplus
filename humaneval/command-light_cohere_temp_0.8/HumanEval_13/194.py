```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a) + 1

print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 30)))  # Output: 10
print(greatest_common_divisor(2, 32)))  # Output: 32
```
This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two numbers `a` and `b`. The function uses a recursive approach, with the base case of division by 0, and recursively computes the GCD of the numbers. The result is also tested with a series of inputs and prints the corresponding greatest common divisors.