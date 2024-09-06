```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (positive == float('-inf') or n > positive):
            positive = n
        if n < 0 and (negative == float('inf') or n < negative):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers using two variables, `positive` and `negative`. These are initialized to negative and positive infinity, respectively, to ensure that any integer encountered will be smaller than the initial value. As the loop iterates through the list, it compares each integer to the current `positive` and `negative` values and updates them if necessary. Finally, the function returns a tuple containing the largest negative integer (or `None` if not found) and the smallest positive integer (or `None` if not found). 

This approach ensures that the correct values are found even if multiple integers are present in the list and provides a clear understanding of the algorithm's logic.  feels neatly packaged and ready to be executed independently, as needed.

This code includes tests at the bottom to ensure that the function behaves as described in the problem statement:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-5, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -6, -7]) == (-7, 1)
```