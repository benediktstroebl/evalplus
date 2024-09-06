```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(divisor(a, b) , greatest_common_divisor(b%a, a))

def divisor(a: int, b: int) -> int:
    for c in range(1, max(a, b)+1):
        if a % c == 0 and b % c == 0:
            return c
```

This code implements a recursive function `greatest_common_divisor` that computes the greatest common divisor of two integers a and b. The function handles the`divisor` function to determine divisibility between the two given numbers and returns the greatest common divisor found after applying the function recursively. The code also handles the particular cases where either of the input numbers is zero, in which case the function returns 0 as there are no common divisors. 

This code is self-contained, meaning it can be run independently and does not require any external functions or classes.