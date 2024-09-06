```python
def max_element(lst):
    if not_numbers(lst):
        return None  # Base case: empty list or all negative
    max_num = max(lst)
    return max_num

def test_max_element(test_list):
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    assert max_element(test_list) == expected

def not_numbers(lst):
    return any(num <= 0 for num in lst)
```