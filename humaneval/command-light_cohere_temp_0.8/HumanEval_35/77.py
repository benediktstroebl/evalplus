```python
def max_element(lst):
    if not_inclusive(lst):
        return max(lst, key=lambda x: (x, -x))
    else:
        return max(lst, key=lambda x: x)

def not_inclusive(lst):
    return all(map(lambda x: x != float('-inf'), lst))

# Unit tests
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert not max_element([5, 3, -5, 2, -3, 3, -100, 1, 2, 3])
assert not max_element([5, 3, -5, 2, -3, -100, 1, 2, 3]) == float('-inf')
```
This function computes the maximum element in a list and also implements a helper function to determine if the list is sorted in increasing order with negative values.  It verifies its tests this script with these two test cases.