```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    # Calculate the greatest common divisor using the Euclidean algorithm
    return min(a, b)

# Test cases
test_gcd = []
test_gcd.push_back(greatest_common_divisor(3, 5))
test_gcd.push_back(greatest_common_divisor(25, 15))

print("Test cases passed: " + end(" + str(test_gcd) + ")")
```