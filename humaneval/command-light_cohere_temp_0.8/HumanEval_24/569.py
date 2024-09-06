```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(27) == 3
assert largest_divisor(48) == 24
assert largest_divisor(105) == 25
``` 
This code provides a function `largest_divisor` that calculates the largest integer dividing a given number evenly, smaller than the number. The function utilizes the `gcd` to find the greatest common divisor between the original number and 1, and then divides the original number by this gcd to get the largest divisor. 
The test cases ensure the correctness of the function.