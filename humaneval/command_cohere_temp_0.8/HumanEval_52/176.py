```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and quickly checks if each item is less than the threshold `t`. It returns `True` if all items are below the threshold, and `False` otherwise. 
Here is a snippet of tests to ensure the function behaves correctly:
```python
# Tests:
assert below_threshold([1, 2, 4, 10], 100), "List should be entirely below threshold"
assert not below_threshold([1, 20, 4, 10], 5), "List should not be entirely below threshold"
``` 
This test suite covers both scenarios presented in the original problem description and ensures that the function `below_threshold` behaves correctly.