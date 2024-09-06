Here's the code:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be given")
    if a == 0:
        return 0
    if b == 0:
        return 0

    while a != 0:
        a, b = b, a // b
    if b == 0:
        return a

    return b
```  The `greatest_common_divisor` function accepts two integers a and b as arguments, and returns the greatest common divisor of a and b. It does so using a testing for edge cases, as well as employing a "dividing" strategy to discover the greatest common divisor.