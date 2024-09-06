```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x + 1)

# Test cases
tests = {
    "Input: [1, 2, 3, 4, 5, 6]
    "Expected Output: [3, 4, 5, 6, 1, 2]"
    pass

# Test using sorted() + lambda
tests. test_ec = [3, 4, 5, 6, 1, 2]
test_ec_result = sort_even(test_ec)
assert test_ec_result == test_ec_expected, "The results do not match."
```