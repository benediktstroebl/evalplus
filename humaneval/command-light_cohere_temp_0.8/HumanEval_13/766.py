```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    return max(divisor(a) ,divisor(b))

def divisor(x):
    if x == 0:
        raise ValueError("Divisor cannot be zero")
    return x
def test():
    a = 3
    b = 5
    print(f"Greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)}")

test()
```