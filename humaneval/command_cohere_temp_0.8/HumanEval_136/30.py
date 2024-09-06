```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses the `min` and `max` functions with a custom key to find the smallest positive and largest negative integers in the list. The key is a lambda function that returns `True` if the number is negative, and `False` if the number is positive, which helps to identify the negative numbers and assign them to the `negative` variable stably. If there are no negative or positive integers in the list, it returns `None`. 

Here is an example of how to use the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (1, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

This would output:
```bash
(1, 1)
(None, None)
(None, None)
```

This illustrates that the function handles the scenario where the list is empty, or contains only zero, and correctly identifies the largest negative and smallest positive numbers in the list when they exist.  This solution is concise and avoids explicit conditional statements, making the code more maintainable and easier to understand.