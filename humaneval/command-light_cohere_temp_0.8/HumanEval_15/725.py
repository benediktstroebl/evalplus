```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test case 1: Test the function with 0
test_case1 = str(string_sequence(0))
print("Test case 1:", test_case1)

# Test case 2: Test the function with a positive integer
test_case2 = str(string_sequence(5))
print("Test case 2:", test_case2)

# Test case 3: Test the function with a negative integer
test_case3 = str(string_sequence(-5))
print("Test case 3:", test_case3)

# Test case 4: Test the function with a large positive integer
test_case4 = str(string_sequence(1000))
print("Test case 4:", test_case4)
```