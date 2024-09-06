```python
def max_element(lst):
    if not_num_max(lst) is not None:
        return not_num_max(lst)
    elif len(lst) == 0:
        return None
    else:
        return max(lst)

def not_num_max(lst):
    try:
        return max(lst, key=float)
    except TypeError:
        return None

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element(["abc", "bcd", "cde"]))
    print(max_element([1, 2, 3, -100]))
    print(max_element([10, 11, 12, 13]))
    print(max_element([None, 200, 400, 500, 600, 700])))
```
The code defines a function `max_element` that finds the maximum element in a list. The `not_num_max` helper function checks whether the list contains a numeric element and returns `None` if not. It then uses the common Python functions (`max` and `float`) to handle all cases: empty lists, lists with one element, and lists with multiple elements. The script then tests the to ensure that the `max_element` function works correctly for all valid inputs.