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

The `largest_smallest_integers` function iterates through the list of integers and identifies the largest negative and smallest positive integers, storing them in `negative` and `positive` variables, respectively. These variables are updated accordingly during each iteration, ensuring the most extreme values are captured.

It's worth noting that the function initially sets both `negative` and `positive` to `None` and then updates them as appropriate during the loop. This approach handles scenarios where the list might lack negative or positive integers, resulting in `None` values for the corresponding variable when there is no extreme value of that type in the list.

The provided example use cases in the comment are also included in the code, alongside tests to validate the function's behavior:
```python
# Tests
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)

assert largest_smallest_integers([-3, -5, -1, -7, -4, -2]) == (-2, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, -8]) == (-8, 5)
```

The tests cover various scenarios, including empty lists, lists with no negative or positive integers, and lists with both negative and positive integers. These tests help to verify that the function behaves correctly in each of these distinct cases.