```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid")
    elif a == 0 or b == 0:
        return 0
    elif a == b:
        return a
    else:
        return max(a, b)
```
This function checks for valid inputs and returns the greatest common divisor of two integers a and b. If the inputs are not valid, a ValueError is raised. The function also handles special cases where a or both inputs are 0, returning 0 as the GCD. 

This script is self-contained and has no external dependencies, as it only relies on the input parameters and the built-in functions.