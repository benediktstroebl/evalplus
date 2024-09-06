Here is a Python script that includes a self-contained function `greatest_common_divisor`, along with unit tests:
```python
import math

def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a < 0 or b < 0:
        raise ValueError("Both numbers should be positive")

    # Calculate gcd using the math.math function
    value
    mathematical method with the fastest execution
    return math.gcd(a, b)

def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    test_gcd()
```
This code defines a `greatest_common_divisor` function that calculates the greatest common divisor using the `math.g` function, which performs the gcd algorithm, which returns the result in O(log(min(a, b))). 

It also includes a `test_gcd` function that contains some assert statements to test the `greatest_common_divisor` function with different inputs, ensuring its correctness. 
The `if __name__ == "__main__":` condition is used to execute the test function when the script is run directly.