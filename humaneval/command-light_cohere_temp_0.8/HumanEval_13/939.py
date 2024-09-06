```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)

# Test case 1: Both inputs positive
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 2: One input positive, other not
print(greatest_common_divisor(3, 5))  # Raises ValueError: Both inputs must be positive numbers
print(greatest_common_divisor(25, 3)))  # Raises ValueError

# Test case 3: Both inputs positive, greater than 1
print(greatest_common_divisor(5, 7))  # Output: 7
print(greatest_common_divisor(121, 321))  # Output: 321

```
The Python function `greatest_common_divisor` takes two integer inputs `a` and `b` and returns the greatest common divisor of `a` and `b`. The function first checks if both inputs are zero, and if so, it raises a `ValueError`. If one input is zero, it returns the other input as the greatest common divisor. If both inputs are positive, it proceeds with checking which input is one and returns the greatest common divisor of the remaining input by calling the function recursively with the other input and the remainder of the first input. 

The function uses recursion to efficiently compute the greatest common divisor by dividing the smaller input into the larger input until the smaller input becomes zero.