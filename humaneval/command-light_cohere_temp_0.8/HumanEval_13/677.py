```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Unit tests
test_greatest_common_divisor = {
    'test_one':  (3, 5),
    'test_two': (25, 15),
    'test_three': (10, 15),
    'test_four': (2, 3),
    'test_five': (5, 7),
    'test_six': (12, 17),
    'test_seven': (20, 35),
    'test_eight': (47, 19),
    'test_nine': (14, 25),
    'test_ten': (27, 19),
}

for test_name, test_values in test_greatest_common_divisor.items():
    calculate_greatest_common_divisor(*test_values)
    assert calculate_greatest_common_divisor(*test_values) == test_values[test_name], f"test {test_name} failed"

```  The Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers using the `gcd` function. The function also includes unit tests to verify its correctness. The unit tests cover a range of scenarios and use the `assert` assertion to check if the function's output matches the expected result.