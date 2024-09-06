```python
def incr_list(lst):
    return [lst[i]+1 for i, x in enumerate(lst)]

# Test cases
test_incr_list = [
    ( [1, 2, 3], [2, 3, 4] ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124])
]

for l, r in test_incr_list:
    assert l == incr_list(l)
    assert r == incr_list(r)
```
This function, `incr_list`, takes a list lst as input and returns a new list with elements from the original list incremented by 1. The function uses the **enumer** to iterate through the list and increment each element by 1. The test cases ensure that the function is working correctly by comparing the output of the function with the expected result for the given input.