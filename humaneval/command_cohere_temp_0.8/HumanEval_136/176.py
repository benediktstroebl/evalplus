```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (n < positive or positive == float('-inf')):
            positive = n
        if n < 0 and (n > negative or negative == float('inf')):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The function `largest_smallest_integers` works by setting the variables `positive` and `negative` to negative and positive infinity respectively. Then, it iterates through the list, checking if any values are larger than `positive` or smaller than `negative`. If so, it updates these values. Finally, it returns a tuple containing these two values, or `None` if there are no positive or negative numbers in the list.

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
```

This would output:
```
(None, 1)
```

This is consistent with the problem statement's examples.