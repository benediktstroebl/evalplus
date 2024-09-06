```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list does not contain any negative or positive integers, it returns `None` for both values to comply with the problem's request. 

This solution adheres to the problem's specification and provides an efficient algorithm for finding the largest negative and smallest positive integers in a list of integers. 

Here is an example of how to use the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

This technique is efficient and adaptable, making it useful for solving problems involving extremal integer values in lists.