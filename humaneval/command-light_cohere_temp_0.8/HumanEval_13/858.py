```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(gcd(a, b), 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"GCD of {a} and {b} is {greatest_common_divisor(a, b)}")
```
This code defines a function gcd that calculates the greatest common divisor using the Euclidean algorithm. The greatest_common_divisor function then applies the same logic to find the greatest common divisor of two input numbers a and b. The output will be the example, in the console will print the greatest common divisor of 25 and 15 which is 5.