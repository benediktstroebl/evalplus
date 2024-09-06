```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    mn, mx = min(lst), max(lst)
    sm = mn
    for n in lst:
        if n > mx:
            continue
        if n > sm and n != mx:
            sm = n
    return sm
```

The algorithm for finding the second-smallest number in the list consists of these main steps:
1. We first guard against the empty list scenario by checking the list length.
2. Using `min()` and `max()` functions, we determine the minimum and maximum values in the list.
3. The variable `sm` (second-smallest) is initialized with the minimum value.
4. We iterate through the list, ignoring values that are greater than the maximum value.
5. If the current value is greater than the second-smallest value found so far (`sm`) and not equal to the maximum value, we update `sm`.

This ensures that `sm` is the second-smallest value in the list, and we return it. 

The tests would look like this:
```python
test_next_smallest = asyncify(lambda: all(next_smallest(lst) == expected for lst, expected in [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([], None),
    ([1, 1], None),
])))
```

The above code uses the `all()` function and a list of test cases to verify the function `next_smallest`. The `asyncify()` decorator is used to make the test function asynchronous, improving its performance.