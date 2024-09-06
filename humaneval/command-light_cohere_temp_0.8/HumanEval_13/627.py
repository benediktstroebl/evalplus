```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    c = 0
    while b > 0:
        if a % b == 0:
            c += 1
        a //= b
    while c < b:
        c += 1
    return c

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(9, 25) == 25
assert greatest_common_divisor(0, 6) == 0
assert greatest_common_divisor(20, 0) == 0
assert greatest_common_divisor(0, 0) == 0
```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of 2 integers a and b. It uses the same loop to find the highest divisor which evenly divides both a and b, until it reaches a smaller number. The test cases cover a following: passing the function with various inputs and checking the output against the expected result. The code is self-contained and provides the functionality to calculate the greatest common divisor of 2 integers.