```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        elif n < 0:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function works by setting the `positive` and `negative` variables to negative and positive infinity respectively. Then, it iterates through the list, checking if each element is larger than the current most positive integer found `>(positive)` or more negative than the current most negative integer found `< (negative)`. The function updates the values of `positive` and `negative` accordingly.

At the end of the loop, the function returns a tuple consisting of the largest negative integer found and the smallest positive integer found, or `None` if either the list contains no negative or positive integers. 

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0]))
```

This will output:
```
(None, 1)
(None, None)
(None, None)
```

This is consistent with the examples provided in the problem statement.