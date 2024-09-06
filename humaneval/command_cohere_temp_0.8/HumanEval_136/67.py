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

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integers encountered. Using `float('-inf')` and `float('inf')` allows for efficient comparison of positive and negative values, respectively. The function returns a tuple with the respective integers if both are valid, and `None` otherwise. 

The following test cases would be useful to ensure the function works as expected:
```python
test_cases = [
    ([2, 4, 1, 3, 5, 7], (None, 1)),  # Positive: 1, Negative: 7
    ([-3, -7, -1, -9, -11], (-11, None)),  # Both present
    ([0, 2, 4, 6, 8], (None, None)),  # No negative integers
    ([-5, -10, -15], (None, None)),  # No positive integers
    ([], (None, None)),  # Empty list
    ([17, -5, 4, 0, -2, 11], (None, 4)),  # Various combinations
]

for lst, expected in test_cases:
    result = largest_smallest_integers(lst)
    assert result == expected, f"Expected {expected}, got {result} for input {lst}"
```

This test suite covers various scenarios, including cases with no negative or positive integers, one of each, or both.