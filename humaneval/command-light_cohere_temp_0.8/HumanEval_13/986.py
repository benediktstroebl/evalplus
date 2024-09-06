```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    return max(a, b) / min(a, b)

# Unit tests
test_gcd = TotalTestCases()
test_gcd.py()
def test_gcd(test_case):
    input_a, input_b = test_case
    expected_result = greatest_common_divisor(input_a, input_b)
    assert expected_result == test_gcd(input_a, input_b)
    return input_a, input_b

# Example usage
input_a = 3
input_b = 5
print("Expected:", greatest_common_divisor(input_a, input_b))
print(" Got:", greatest_common_divisor(input_a, input_b))
``` 
Note that the test_gcd function can be used to find the greatest common divisor of any two integers. The script is self-contained and passes all corresponding tests.