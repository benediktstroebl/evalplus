```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [i+1 for i in l]
    return l

#Test cases
test_incr_list = [
    [
        ("List", lambda: "List" not in l),
        (["1", "2"], lambda: l != [1,2]),
        (list([5, 3, 5, 2, 3, 5]) , lambda: "List" in l and l != [5, 3, 5]),
        ({"text": "Hi", "items": [1, 2, 3]}, lambda: l != [1, 2, 3]),
        (set([1, 2, 3]), lambda: "List" in l and l != set),
        ([1,2,3], lambda: isinstance(l, list)),
        ([1,2,3], lambda: l != [1, 2, 3])
    ]

#Call function
for test in test_incr_list:
    assert incr_list(test[1]) == test[2]
 ```