```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1:] + [0]] + lst[-1:]

# Test cases
test_sort_even = [
    ()
    [list("hello"), 2, 3],
    [5, 6, 3, 4]
]

# Main code
for testcase in test_sort_even:
    assert sort_even(testcase) == testcase  # Test the function
```