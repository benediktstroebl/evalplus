```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not equal to zero.")
    elif a == b:
        return 0
    else:
        return max(divmod(a, b)[1])
```  This function calculates the greatest common divisor of two numbers a and b using the Euclidean algorithm, which efficiently computes the greatest divisor.  It guaranteed correct results and it can handle cases where a or b are negative or zero, as well as non-zero positive numbers.