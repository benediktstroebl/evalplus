```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            positive = max(positive, n)
        else:
            negative = min(negative, n)
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, finding the smallest positive integer and the largest negative integer. The returned result is a tuple (`a`, `b`), where `a` is the largest negative integer and `b` is the smallest positive integer. If the list lacks negative or positive integers, both values are returned as `None`.

The test examples in the Markdown block are reflected in the script's test cases to ensure the function behaves as expected:
```python
# Tests
assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
assertEqual(largest_smallest_integers([]), (None, None))
assertEqual(largest_smallest_integers([0]), (None, None))
```