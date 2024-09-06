```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each item in the input `list` `l` and verifies if each item is less than the given `threshold` `t`. If all items are less than the threshold, the function returns `True`, otherwise, it returns `False`.

Here is a test case to ensure that the above function is correct:
```python
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
```