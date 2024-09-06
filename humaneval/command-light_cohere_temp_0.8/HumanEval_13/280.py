```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is not a number.")
    return max((i) for i in range(1, min(a, b) + 1) if all(gcd(i, a) == gcd(i, b)))

def gcd(x, y): return x if y == 0 else gcd(y, x % y)

def test():
    a = 3
    b = 5
    print("The greatest common divisor of", a, "and", b, "is", greatest_common_divisor(a, b))

test()
```