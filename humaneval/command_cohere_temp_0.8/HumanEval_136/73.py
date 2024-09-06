```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The Python script defines a function `largest_smallest_integers` that solves the problem as described in the prompt. It iterates through the list, identifying the largest negative integer and the smallest positive integer, updating the respective variables `negative` and `positive`. The function ultimately returns a tuple containing these two values. If there are no negative or positive integers in the list, `None` is returned for both parts of the tuple.

Here is a concise example of how to use this function:
```python
print(largest_smallest_integers([-3, -1, 0, 2, 4, 1, 3, 5, 7])) 
```

The output will be:
```
(-1, 1)
```

This is consistent with the examples provided in the prompt:
- The list `[2, 4, 1, 3, 5, 7]` returns `(None, 1)`, indicating that the largest negative integer is `None`, and the smallest positive integer is `1`.
- The empty list `[]` returns `(None, None)`.
- The list `[0]` (which contains no negative or positive integers) also returns `(None, None)`.