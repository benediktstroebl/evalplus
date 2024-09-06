```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    else:
        return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test cases
MAX_ELEM = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(MAX_ELEM) == 123
assert max_element([]) == float('-inf')
assert max_element([1, 2, 3]) == 3
assert max_element([4, 4, 4]) == 4
assert max_element([1, -2, 3]) == 3
```
The function max_element computes the highest element in a list. The auxiliary function not_positive determines whether the list contains only positive values, returning True if so, and False otherwise. The main test suite includes a variety of test cases, including lists with no maximum element, lists with positive elements only, and lists with an overall maximum.