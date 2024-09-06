```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    elif a == 0 or b == 0:
        return 0
    else:
        return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The GCD of {a} and {b} is {greatest_common_divisor(a, b)} which is {gcd(a, b)}")
```
This code defines a function gcd that calculates the greatest common divisor using the Euclidean Algorithm. The main function then demonstrates the use of the gcd function by finding the GCD of a and b.

The output of the above code will be: 
```
The GCD of 25 and 15 is 5 which is the gcd(25, 15)
```