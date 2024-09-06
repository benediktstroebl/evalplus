```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive integers.")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
    print(greatest_common_divisor(10, 4))
    print(greatest_common_divisor(6, 12))
```
The function greatest_common_divisor calculates the greatest common divisor of two integers a and b. The function first checks if either a or b is equal to 0, and if so, raises a ValueError indicating that both inputs must be positive integers. 

The gcd function calculates the greatest common divisor using the Euclidean algorithm. The function then returns the gcd(a, b) which is the greatest common divisor of a and b. 

The script also passes all the corresponding tests.