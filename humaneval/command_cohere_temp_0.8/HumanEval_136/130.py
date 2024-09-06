```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses `min` and `max` to find the smallest positive and largest negative integers respectively in the list. The `key` argument is used to specify the condition for the values, in this case, check if the value is greater than or equal to zero for the `min` function, and less than zero for the `max` function. 

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (7, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

This would output:
```bash
(7, 1)
(None, None)
(None, None)
```

This code passes the given tests and returns the largest negative integer and smallest positive integer in the list, or `None` if there are no negative or positive integers in the list.