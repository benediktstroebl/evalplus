```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")

    # Calculate GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b

    return a

# Unit tests
def test GreatestCommonDivisor():
    a = 3
    b = 5

    assert greatest_common_divisor(a, b) == 1
    assert greatest_common_divisor(5, 3) == 1
    assert greatest_common_divisor(15, 25) == 5

if __name__ == "__main__":
    test GreatestCommonDivisor()
``` 
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers. The function undergoes input validation and utilizes the Euclidean algorithm to efficiently compute the GCD. Additionally, the code includes unit tests, ensuring that the function behaves correctly and provides the expected results for various inputs.