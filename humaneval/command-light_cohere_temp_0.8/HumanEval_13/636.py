```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    return max(a, b) / gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f'The greatest common divisor of {a} and {b} is {gcd(a, b)}: {gcd(a, b)}')
```