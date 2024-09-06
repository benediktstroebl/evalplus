```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

# Test case 1
test_case1 = 10  # int value for n
result = string_sequence(test_case1)
assert result == "0 10 11 12 13 14"

# Test case 2
test_case2 = 0  # int value for n
result = string_sequence(test_case2)
assert result == "0"

# Test case 3
test_case3 = "Hello World"  # string value for n
result = string_sequence(test_case3)
assert result == "Hello World"

# Test case 4
test_case4 = [1, 2, 3]  # List of numbers for n
result = string_sequence(test_case4)
assert result == "[0 1 2 3]"
```