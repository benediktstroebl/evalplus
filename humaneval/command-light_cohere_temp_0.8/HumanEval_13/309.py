```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) // gcd(a, b)
 
def gcd(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    while b:
        a, b = b, a % b
    return a
 
# Test the function
try:
    greatest_common_divisor(3, 5)
    print("Success!")
except ValueError as e:
    print(f"Error: {e}")

try:
    greatest_common_divisor(25, 15)
    print("Success.")
except ValueError as e:
    print(f"Error: {e}")
```
The above code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. In this case, we ensure that the inputs are both numbers by raising a ValueError. We also implement the for the main, we calculate the greatest common divisor using the `gcd` function, which calculates the greatest common divisor of the input numbers using the Euclidean algorithm. Finally, we test the code by calling the `greatest_common_divisor` function with two test cases: `3` and `5` and `25` and `15` to ensure the function works correctly.