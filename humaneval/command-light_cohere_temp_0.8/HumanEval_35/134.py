```python
def max_element(lst):
    if not_max == lst[0]: return lst[0]
    if lst[0] < 0: return -1
    if len(lst) == 1: return lst[0]
    if lst[-1] >= lst[0]: return lst[-1]
    return max(max_element(sub) for sub in lst[1:])

def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

not_max = [1, 2, 3]
test_max_element()
```

The function `max_element` takes a list `lst` as input and returns the maximum element in the list. The function uses a iterative approach to find the maximum element. It also uses a test cases to check the functionality of the `max_element` function.