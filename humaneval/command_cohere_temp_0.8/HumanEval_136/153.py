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

The `largest_smallest_integers` function works by setting the initial values of `positive` and `negative` to negative and positive infinity respectively. This is done to simplify the comparison logic, as any integer value will be less than `negative` and greater than `positive` when initially comparing.

Then, it iterates over the list `lst`. When a positive integer is found that is smaller than the current `positive` or `positive` is initially negative infinity, the value of `positive` is updated. Similarly, when a negative integer is found that is larger than the current `negative` or `negative` is initially positive infinity, the value of `negative` is updated.

At the end, the function returns a tuple containing the largest negative integer and the smallest positive integer from the list, or `None` if there are no negative or positive integers in the list. 

The behavior is validated through these tests:
1. `largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)` -- This tests the example where only positive integers are present, and the largest is correctly identified.
2. `largest_smallest_integers([]) == (None, None)` -- This tests the empty list case, confirming that both values in the tuple return None.
3. `largest_smallest_integers([0]) == (None, None)` -- This tests when the list contains only zero, confirming that both values in the tuple return None. 

Let me know if you'd like any adjustments to the code! I can also provide more test cases if you'd like to test against edge cases and specific scenarios.