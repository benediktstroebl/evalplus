```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    list comprehension:
    for x, y in l:
        if x + y == 0:
            return True
    """

def test():
    """
    Test function to check if the function pairs_sum_to_zero returns True for the given list.
    """
    list of integers [1, 3, 5, 0]
    """
    return pairs_sum_to_zero([1, 3, 5, 0]) == True

def test2():
    """
    Test function to check if the function pairs_sum_to_zero returns True for the given list
    """
    return pairs_sum_to_zero([1, 3, -2, 1]) == True

def test3():
    """
    Test function to check if the function pairs_sum_to_zero returns True for the given list
    """
    return pairs_sum_to_zero([1, 2, 3, 7]) == True

def test4():
    """
    Test function to check if the function pairs_sum_to_zero returns True for the given list
    """
    return pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

def test5():
    """
    Test function to check if the function pairs_sum_to_zero returns True for the given list
    """
    return pairs_sum_to_zero([1]) == False
```
The above Python script contains a self-contained function `pairs_sum_to_zero` that checks whether two distinct elements in a list sum to zero. The `test` function is used to test the function with various input lists, and the `test2` function is used to test the function with a specific edge case.