```python
def max_element(lst):
    if not_list(lst):
        raise ValueError("Input must be a list")
    return max(lst)

# Test the function with various input types
tests = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element = max_element(tests)
print("Maximum element:", test_max_element)
```