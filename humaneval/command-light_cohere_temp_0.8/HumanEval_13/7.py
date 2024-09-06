```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return max(a, b) / __gcd__(a, b)

def __gcd__(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(89, 5))  # Output: 23
    print(greatest_common_divisor(123, 45))  # Output:567
    print(greatest_common_divisor(0, 4))  # Output: 0
```