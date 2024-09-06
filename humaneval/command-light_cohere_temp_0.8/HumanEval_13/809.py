```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input must be a positive integer")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    if not a: return b
    if not b: return a
    return max(a, b)

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    test_greatest_common_divisor()
``` 
This code defines a `greatest_common_divisor` function that calculates the greatest common divisor of 2 integers passed to it. It also includes a test function to verify the correctness of the `greatest_common_divisor` function with a few test cases. 
Please note that the test cases can be easily expanded to cover more scenarios and ensure the function works correctly for various inputs.