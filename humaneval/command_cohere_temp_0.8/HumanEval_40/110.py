```python
def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    counter = Counter(lst)
    
    # Filtering elements that can form a sum of zero with another element in the list
    candidates = [x for x in counter if counter[x] >= 2 and x == -counter[x]]
    
    # Checking if there are exactly two candidates left and one of them is -x
    return len(candidates) == 2 and (-x in candidates for x in candidates if x != -x)
```

The problem is solved using a combination of Python's `Counter` and filtering techniques. `Counter` is utilized to count the number of occurrences of each element in the input list. Elements that appear more than once and have a count that is equal to their negation (-x) are considered candidates that can potentially form a sum of zero. These candidates are filtered and checked to ensure there are exactly two of them left, one of which is `-x`. If this condition is met, the function returns `True`, indicating the presence of three distinct elements that sum up to zero. Otherwise, it returns `False`.