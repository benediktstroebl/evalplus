```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    if a == b:
        return a
    return max(a, b) if a != b else 0

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(4, 6) == 0
assert greatest_common_divisor(10, 25) == 0
assert greatest_common_divisor(36, 12) == 12
 ``` 
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. The function uses a approach that compares the two inputs, and returns 0 if they are equal or the greater of the two values. The function also raises a ValueError if either input is 0.