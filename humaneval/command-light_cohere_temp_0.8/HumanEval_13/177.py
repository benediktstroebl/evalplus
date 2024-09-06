```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Use Euclid's Algorithm
    temp = b
    while a % temp == 0:
        b = temp
    temp = a
    while b % temp == 0:
        a = temp

    return a
```  This function takes two integers a and b as input and returns the greatest common divisor of a and b respectively. 

This is a self-contained Python function that takes a and b as input and returns the greatest common divisor of a and b.