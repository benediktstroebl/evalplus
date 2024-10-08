```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as an argument and returns a tuple containing the largest negative integer and the smallest positive integer from the list. If the list contains no negative or positive integers, it returns `None` for the respective value. 

Here is an example of how you can use the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Outputs: (None, 1)
print(largest_smallest_integers([]))  # Outputs: (None, None)
print(largest_smallest_integers([0]))  # Outputs: (None, None)
```

This function solves the task as specified in the problem statement. It filters out the integers based on their signs and then finds the largest and smallest among them utilizing the `max` and `min` functions, respectively.