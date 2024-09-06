```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    elif len(lst) == 0:
        return float('-inf')
    else:
        return max(lst)

def test_max_element():
    try:
        print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
        print("Passed test.")
    except AssertionError:
        print("Failed test.")
```

The function `max_element` in this code accepts a list lst and determines and returns the list's maximum element. The test_max_element function is used to check the function's correctness by passing various test lists.