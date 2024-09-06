```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "One or both inputs is not a number"
    if a == 0 or b == 0:
        return "Both inputs are zero"
    return max(a, b) / gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print("The greatest common divisor of", a, "and", b, "is", greatest_common_divisor(a, b))
```
The function greatest_common_divisor calculates the greatest common divisor of two numbers a and b. It uses the specific function gcd to calculate the greatest common divisor using the Euclidean Algorithm. The function also handles edge cases where one or both inputs are not numbers or are zero, returning appropriate error messages.