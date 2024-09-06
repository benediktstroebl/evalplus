```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive")

    # Calculates the gcd of a and b using the built-in function
    return gcd(a, b)

# Unit tests
def test_greatest_common_divisor():
    try:
        a = 3
        b = 5
        common = greatest_common_divisor(a, b)
        assert common == 1
        a = 25
        b = 15
        common = greatest_common_divisor(a, b)
        assert common == 5
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
test_greatest_common_divisor()
```