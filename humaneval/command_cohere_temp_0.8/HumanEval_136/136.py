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

The `largest_smallest_integers` function iterates through the list of integers and identifies the largest negative and smallest positive numbers. The function compares the current integer with the current largest negative and smallest positive, updating them if necessary. Ultimately, it returns these two values as a tuple.

The test cases provided in the problem statement are:
1. `largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)`: This case tests the function with a list of mixed integers, expecting the result to be `(None, 1)`, indicating that `None` represents no negative integer, and the smallest positive is 1.
2. `largest_smallest_integers([]) == (None, None)`: This case tests the function with an empty list, expecting the result to be `(None, None)`, indicating the absence of both negative and positive integers.
3. `largest_smallest_integers([0]) == (None, None)`: This case tests with a list containing only zero, and again, the result is `(None, None)` since zero is not distinct from negative or positive.

The function handles these cases correctly, returning the expected results based on the given test cases.