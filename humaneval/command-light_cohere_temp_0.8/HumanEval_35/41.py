```python
def max_element(lst):
    return max(lst)

# Test the function with different lists and ensure the result matches the expected maximum value
test_max_element=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123
test_max_element_error = [-5, 2, 3, -5]
try:
    assert max_element(test_max_element_error) == 2
except AssertionError as e:
    print("Error:", e)
```