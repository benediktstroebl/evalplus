```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("One or both arguments is empty")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    if a == 0 or b == 0:
        return 0
    # prime factorization using factor() method of math library
    pa = math.fact()
   (a)
    pb = math.fact()(b)
    # Find highest common divisor using the loop
    hcd = 1
    while pa <= pb:
        if b % pa == 0:
            b = b // pa
            hcd = hcd * pa
        pa += 1
    return hcd
```