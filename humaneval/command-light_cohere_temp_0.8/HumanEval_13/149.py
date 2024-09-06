```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    # Checks for divisibility
    if a > b or a < 0 or b < 0:
        return "Error: Input values are not valid integers"

    # Initialize a and b with their maximum value to continue checking divisibility
    temp = max(a, b)
    div = 1

    while div <= temp:
        if temp % div == 0:
            # If the current number is divisible by the current divisor, find the GCD
            gcd = temp // div
            return gcd

        div += 1

    return 0
```