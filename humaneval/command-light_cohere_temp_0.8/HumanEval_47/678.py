```python
def median(l: list):
    """Return median of elements in the list l."""
    return (getmedian(l) + getmedian(reverse(l)) )/2 or (len(l) + 1) / 2
def getmedian(lst):
    return (sum(sorted(lst)) + sorted((lst[::index:]) for index in range(len(lst))))) / 2
# Tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([9, 2, 4, 8, 1]) == 2.5
``` 
Now, the test suite includes additional test cases to check the correctness of the median function.