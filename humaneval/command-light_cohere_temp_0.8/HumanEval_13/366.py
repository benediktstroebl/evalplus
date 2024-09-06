```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    elif a == 0 or b == 0:
        return 0
    else:
        return max(gcd(a, b), 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The GCD of {a} and {b} is: {greatest_common_divisor(a, b)}")
```