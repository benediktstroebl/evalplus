```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) >= 1, "List must have at least one element"
    assert all(isinstance(x, (int, float)) for x in l), "List must only contain numbers"
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Test the function with a variety of inputs
med_values = median([10, 20, 4, 6, 3, 1, 2, 7, 8, 5])
assert median([10, 20, 4, 6, 3, 1, 2, 7, 8, 5]) == med_values, "Median calculation failed"
assert median([]) == 0, "Empty list should return 0"
assert median([5, 10, 10, 5]) == 5, "Incorrect handling of odd number of elements"
assert median([1000, 4000, 6000]) == 6000, "Incorrect handling of large numbers"

I hope this was helpful.