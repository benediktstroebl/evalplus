Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
import math
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    else:
        return math.sqrt(max((a **a, b))
```
This function uses the sqrt function to return the greatest common divisor of two integers a and b, using the max function to return the greater of the two integers. The function also handles the case where either a or b is 0, in which case it returns 0.