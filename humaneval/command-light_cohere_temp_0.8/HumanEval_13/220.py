```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be greater than zero")
    return math.sqrt(min(a, b)) if a > b else b

test_function = greatest_common_divisor
test_passed = True
try:
    test_passed = test_function(3, 5)
    print(test_passed)
    test_passed = test_function(25, 15)
    print(test_passed)
except ValueError as e:
    print("Caught error:", str(e))
```