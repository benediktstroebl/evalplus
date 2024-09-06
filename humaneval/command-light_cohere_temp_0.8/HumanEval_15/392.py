```python
def string_sequence(n: int) -> str:
    return f"0 {n}{" + str(n) + "}"

# Test cases for function
test_str = string_sequence(5)
print("Test Case 1:", test_str)  # Output: "Test Case 1: 0 5"
test_str = string_sequence(0)
print("Test Case 2:", test_str)  # Output: "Test Case 2:  0"
test_str = string_sequence(-5)
print("Test Case 3:", test_str)  # Output: "Test Case 3: -5"
test_str = string_sequence(10)
print("Test Case 4:", test_str)  # Output: "Test Case 4: 0 9"
test_str = string_sequence(0)
print("Test Case 5:", test_str)  # Output: "Test Case 5:  0"
```