```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(3, 15))   # Output: Raises ValueError
print(greatest_common_divisor(1, 5)))   # Output: Raises ValueError
print(greatest_common_divisor(27, 3))   # Output: Raises ValueError
```  This Python code defines a function called greatest_common_divisor that calculates and returns the greatest common divisor of two input integers a and b. It employs basic input validation and falls into three categories: if either a or b is zero, it raises a ValueError, if b is 1, it returns a, if either a or b are 1, it returns b, and if both a and b are greater than 1, it recursively calls itself with the other input divided by the current value of a. Roman the process in the way on the integers.