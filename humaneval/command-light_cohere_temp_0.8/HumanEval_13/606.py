```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("In arguments a and b must be numbers")

    while b != 0:
        a, b = b, a % b

    return a

# Test the function
# expect expression to test for correct function
# call greatest_common_divisor(5, 2) -> 2
# call greatest_common_divisor(30, 15) -> 15
```
The function returns the greatest common divisor of two integers a and b, and handles the case where either argument is not a number. It uses the basic trial and error handling to ensure the function meets its specifications.