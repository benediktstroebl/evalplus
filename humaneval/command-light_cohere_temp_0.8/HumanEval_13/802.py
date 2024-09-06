```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not equal to 0")
    elif a == b:
        return 0
    else:
        return max(gcd(a, b), 1)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
    print(greatest_common_divisor(5, 5))
```
This code defines a function gcd that calculates the greatest common divisor of two numbers using the Euclidean Algorithm, then a function greatest_common_divisor that uses the gcd function and tests cases where the inputs are 0, equal, or negative numbers. 

The main part of the code prints the result of calling the greatest_common_divisor function with test cases.