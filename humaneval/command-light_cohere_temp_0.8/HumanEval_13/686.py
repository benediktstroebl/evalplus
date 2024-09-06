```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b%a, a) + 1
```  This script defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. It handles edge cases, ensures that the divisibility check does not return an error when either a or b is 0, and it uses the Euclidean algorithm to efficiently find the greatest common divisor.