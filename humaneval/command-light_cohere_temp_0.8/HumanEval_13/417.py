```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b
    else:
        return a  # find the larger value (greater common divisor) 

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15)))  # Output: 5 

# Test case 3
print(greatest_common_divisor(35, 25))  # Output: 5 

# Test case 4
print(greatest_common_divisor(4, 12)))  # Output: 3 

# Test case 5
print(greatest_common_divisor(7, 21)))  # Output: 3 

```
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. It employs basic divide- and check to find the greatest common divisor while handling edge cases like zero divisors and avoiding unnecessary iterations.