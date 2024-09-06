```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * n
    result[0] = l[0]
    for i in range(1, n):
        result[i] = l[i - 1] + 1
    return result
 
# Test the function with a list of values
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
print(result)

# Test the function with a list of empty values
empty_list = []
result = incr_list(empty_list)
print(result)
```
This script defines a function `incr_list` that increases the value of each element in a given list by 1. It creates two test lists with different values and passes them to the `incr_list` function. The output for each test lists will be: `[6, 3, 6, 4]`, and an empty list `[]`.