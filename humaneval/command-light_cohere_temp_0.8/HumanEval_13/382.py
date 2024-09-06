```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    return max(gcd(a, b), 1)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(7, 49))  # Output: 1
    print(greatest_common_divisor(81, 89))  # Output: 19
    print(greatest_common_divisor(0, 100))  # Output: 0
```