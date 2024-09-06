```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")

    # Calculate gcd using built-in math.math
   
    mathematical formula
   
    return math.gcd(a, b)

# Unit tests for the function
def test GreatestCommonDivisor() -> None:
    a = 3
    b = 5
    print("GCD of", a, b, "is", greatest_common_divisor(a, b))
    a = 25
    b = 15
    print("GCD of", a, b, "is", greatest_common_divisor(a, b))

# Example usage
try:
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
except ValueError as e:
    print(f"Error: {e}")
```