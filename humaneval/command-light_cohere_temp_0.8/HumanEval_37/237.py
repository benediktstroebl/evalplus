```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    :param lst: list
    :return: list
    """
    lst[:] = sorted(lst, key=lambda x: x if x % 2 else x+1)
    return lst

# Test cases
tests = [
    "Input: [1, 2, 3, 4, 5, 6]
        Expected Output: [1, 2, 3, 4, 5, 6]
    ,
    "Input: [5, 6, 3, 4]
        Expected Output: [3, 6, 5, 4]
    ,
    "Input: [3, 6, 5, 4]
        Expected Output: [3, 6, 5, 4]
    ]
```