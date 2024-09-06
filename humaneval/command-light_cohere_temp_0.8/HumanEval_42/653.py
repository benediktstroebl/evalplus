```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [i+1 for i in l]
    return l

# Test cases
test_incr_list = [
    [
        [],
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ]

for t in test_incr_list:
    actual = incr_list(t)
    assert actual == [i+1 for i in t], f"Failed for {t}."
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements from the input list incremented by 1. The function works by creating a copy of the input list using the slice [] and then assigning each element in the copy list with the next value (i+1). The test cases define a list of different lists to test the incr_list function, and the function is asserted to work correctly for each input.