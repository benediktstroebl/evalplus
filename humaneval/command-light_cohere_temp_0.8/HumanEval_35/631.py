```python
def max_element(lst):
    return lst[0] if len(lst) == 1 else max(lst[1:], lst[0])

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_result = max_element(test_max_element)
should_be = 123

assert test_result == should_be
```