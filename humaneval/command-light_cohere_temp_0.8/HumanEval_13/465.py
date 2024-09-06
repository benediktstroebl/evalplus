```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    else:
        return abs(b)

# Test cases
test_cases = [(3, 5), (25, 15), (2, 4), (8, 7), (6, 12)]
for test_case in test_cases:
    print(f"Case {test_case[0]}: GCD is {test_case[1]}")
    print(greatest_common_divisor(test_case[0], test_case[1]))
```  This code defines a function that computes the greatest common divisor of two integers, testing various inputs and outputting the result.