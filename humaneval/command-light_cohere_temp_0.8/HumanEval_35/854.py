```python
def max_element(lst):
    if not_list(lst):
        raise ValueError("Input must be a list")
    return max(lst)

# Basic tests
test_max_element = [1, 2, 3]
assert max_element(test_max_element) == 3

# Edge cases
test_max_element = [-5]
assert max_element(test_max_element) == -5

test_max_element = [5, 3, -5]
assert max_element(test_max_element) == 3

# Sorted lists
test_max_element = [0, 123, 1, 2]
assert max_element(test_max_element) == 1

test_max_element = [-3, -2, -5, 0]
assert max_element(test_max_element) == 0

# Invalid inputs
try:
    max_element([1, 2, 3])
except ValueError as e:
    print(f"Error: {e}")
```