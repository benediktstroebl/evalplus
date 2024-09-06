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
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(7, 21))  # Output: 1
    print(greatest_common_divisor(93, 61)))  # Output: 13
    print(greatest_common_divisor(10, 90))  # Output: 5
    print(greatest_common_divisor(3333, 888))  # Output: 21
```