```python
def incr_list(lst):
    lst[:] += [1]
    return lst

# Test cases
test_incr_list = [
    zip(
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        lambda l: l[:] == l
    )
]

# Function call
incr_list(test_incr_list)
```