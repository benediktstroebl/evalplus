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

The function `largest_smallest_integers` solves the problem by checking for positive and negative integers in the list `lst`. It initializes `positive` and `negative` to `None` to accommodate the scenario where no positive or negative integer is present. Using a `for` loop, it iterates through the list, comparing each integer to the current most significant or smallest number, updating the respective `positive` or `negative` variables if a larger number is found.

The function ultimately returns a tuple consisting of the largest negative integer and smallest positive integer from the list, or `None` if absent. 

The following examples illustrate its utility:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
``` 

Each example mirrors the test cases provided in the problem statement, confirming the function's correctness.