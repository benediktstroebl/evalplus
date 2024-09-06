```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        gcd = greatest_common_divisor(b, a % b)
        return gcd
```  This function calculates the greatest common divisor using recursion and returns the result.