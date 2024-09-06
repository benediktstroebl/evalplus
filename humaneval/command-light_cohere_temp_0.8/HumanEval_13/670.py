```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers. It employs the use the approach by finding the greatest number and then dividing by the greatest common divisor of the input numbers. It also defines a gcd function to calculate the greatest common divisor. The main function then prints the result for the given test cases.