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

The following test cases would be helpful to validate the function:
```python
test_cases = [
    ([2, 4, 1, 3, 5, 7], (None, 1)), 
    ([], (None, None)), 
    ([0], (None, None)),
    ([-5, -10, -3, -2, -7, -4], (-2, None)),
]

for lst, expected in test_cases:
    result = largest_smallest_integers(lst)
    assert result == expected
```

This script ensures the function handles all the edge cases as mentioned in the problem statement.  The unit tests ensure that the function works correctly for a variety of scenarios.  If needed, I can explain the code in further detail or adjust it according to any specific requirements.