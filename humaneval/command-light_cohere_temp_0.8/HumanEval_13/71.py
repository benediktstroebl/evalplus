```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of inputs must be a positive integer")
    if a == 0:
        return 0
    if b == 0:
        return 0

    # If a is prime, it's the largest divisor
    if a % b == 0:
        return b

    # If b is prime, it's the largest divisor
    return a

 ```