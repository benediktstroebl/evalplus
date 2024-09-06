```python
def max_element(lst):
    if not_numbers(lst):
        raise ValueError("Input list contains non-numeric values")
    return max(lst)

def not_numbers(lst):
    return all(type(num) == int for num in lst)

test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_list)
assert result == 123
```