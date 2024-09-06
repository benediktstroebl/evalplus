```python
def median(l):
    """Return median of elements in the list l."""
    return (max((x for x in l[l.count(1) if x != l[-1]) +
            max((x for x in l[1:l.count(1) if x != l[0]))) / 2.0
```

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([10, 10, 10]) == 10.0
assert median([100, 200, 300]) == 200.0
```
This Python code defines a function called median that computes the median value of a list of numbers. The function uses list comprehension and indexing to identify the middle values of the list and then returns the median as the average of these middle values divided by 2. 
The test cases verify the correctness of the median function by passing various lists and checking if the returned median value matches the expected result.