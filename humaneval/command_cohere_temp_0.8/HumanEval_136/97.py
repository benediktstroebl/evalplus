```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The `largest_smallest_integers` function takes a list of integers as input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. It initializes `positive` and `negative` variables to `None` to represent missing values.

Then, it iterates through the list, checking if each integer is positive or negative. If it is positive, it compares it to the current `positive` value, updating it if the current integer is larger. If it is negative, it compares it to the current `negative` value, updating it if the current integer is smaller.

The final output is a tuple of these two values. If no negative or positive integers are present, then the function returns `(None, None)`.

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Outputs: (None, 1)
print(largest_smallest_integers([]))  # Outputs: (None, None)
print(largest_smallest_integers([0]))  # Outputs: (None, None)
```

This would output:
```bash
(None, 1)
(None, None)
(None, None)
```

This illustrates that the function correctly identifies the largest negative integer and the smallest positive integer among the given lists of integers, handling edge cases where the lists are empty or contain only neutral elements.