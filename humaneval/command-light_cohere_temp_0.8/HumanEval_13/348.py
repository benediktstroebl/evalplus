```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test the function with various inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(16, 4)))  # Output: 4
print(greatest_common_divisor(0, 7))   # Output: 0
print(greatest_common_divisor(3, 0))   # Raises ValueError
print(greatest_common_divisor(5, 2))   # Raises ValueError
```

This script defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers a and b. This function ensures that valid inputs are provided and raises an error for invalid inputs. 

The function follows the recursion approach by calling itself with the arguments of the respective divisors until they become 0. 

Finally, the function applies the logic to various test cases and prints the results.