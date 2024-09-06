```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Invalid input.

    if a number_order(a) != number_order(b):
        return "Both inputs must be positive integers."

    if a == 0:
        return "A is zero, cannot find a common divisor."

    max_div = max( (a, b) )
    for i in range(1, max_div):
        if a % i == 0 and b % i == 0:
            return i

    return "Could not find a common divisor greater than both inputs."
```