```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and quickly compares each item to the threshold value `t`. It then returns `True` if all items are below the threshold, and `False` otherwise.

Here is a test case to ensure the function is operating properly:
```python
def test_below_threshold():
    # True case
    assert below_threshold([1, 2, 4, 10], 100) == True

    # False case
    assert below_threshold([1, 20, 4, 10], 5) == False

test_below_threshold()
```

The function passes both test cases, as expected.