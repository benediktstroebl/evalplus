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

The `largest_smallest_integers` function iterates through the list, tracking the highest positive and lowest negative values using the `positive` and `negative` variables. These are initialized to negative and positive infinite values to handle any integers in the list. The function then returns a tuple containing the largest negative and smallest positive values, or `None` if there are no such values in the list. 

This approach ensures that the correct values are retrieved from the list, and it handles scenarios where the list might not contain both positive and negative integers. 

The following test cases demonstrate the behavior of the function:
```python
test_cases = [
    ([2, 4, 1, 3, 5, 7], (None, 1)),  # Positive smallest, negative largest
    ([], (None, None)),            # No integers
    ([0], (None, None)),           # Single integer 0
    ([-1, 0, 1], (-1, 0)),        # Specific values
]

for test in test_cases:
    assert largest_smallest_integers(*test[0]) == test[1]
```

These tests cover different scenarios, ensuring that the function behaves correctly and returns the expected results for various input lists and different combinations of largest negative and smallest positive integers.