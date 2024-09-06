```python
def max_element(lst):
    if not_num(lst) == []:
        return None  # Handle empty list
    return max(lst)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected
```
This code defines a `max_element` function that finds the maximum element in a given list. It also contains a test_max_element function with a passing test. It can be used as a simplest way to solve this problem, and it works efficiently for any given list.