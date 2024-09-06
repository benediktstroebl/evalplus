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

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integer so far. Using `float('-inf')` and `float('inf')` allows us to handle the cases of no positive or negative integers in the list. The function returns a tuple (`a`, `b`) with the largest negative integer and the smallest positive integer, or `None` for either part if none are found. 

The following example illustrates its usage:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
```

Output:
```
(None, 1)
(None, None)
(None, None)
```

This shows the function's capabilities, from handling filled lists to empty ones, due to the smart use of `float('-inf')` and `float('inf')`.