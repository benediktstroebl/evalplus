```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the built-in `all` function to iterate over each element in the input list `l` and compare it to the threshold value `t`. It then returns `True` if all elements in the list are below the threshold, and `False` otherwise.

Here is a simple test case to ensure the function is working as intended:
```python
assert below_threshold([1, 2, 4, 10], 100), "Expected [1, 2, 4, 10] to be below threshold 100"
assert not below_threshold([1, 20, 4, 10], 5), "Expected [1, 20, 4, 10] not to be below threshold 5"
```