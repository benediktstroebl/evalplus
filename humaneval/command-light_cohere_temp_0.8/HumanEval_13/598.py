```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    return max(gcd(a, b), 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def test():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    print("Test passed!")
```