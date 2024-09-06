```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b) + 1
``` 
This code defines a function, `greatest_common_divisor`, which computes the greatest common divisor of two integers a and b. The function uses a recursive approach, dividing the larger number by the remainder of the division of the smaller number.