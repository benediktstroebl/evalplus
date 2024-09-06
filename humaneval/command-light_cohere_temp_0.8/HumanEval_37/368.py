```python
def sort_even(lst):
    """This function sorts the even indices of a list l, and keeps the values of l at those indices"""
    return lst[:len(lst)//2] + lst[-len(lst)//2:]

# Test cases
test_sort_even = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [10, 11, 12],
    [15, 16, 17]
]

# Run the function and verify the results
for x in test_sort_even:
    actual = sort_even(x)
    expected = [3, 6, 5, 4]
    assert actual == expected, "Test case failed: " + str(x)
```