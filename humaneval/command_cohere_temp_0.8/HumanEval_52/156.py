```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True` and `False` otherwise, returning the overall result of the below-threshold check for the list `l` with respect to the threshold `t`. 

Here's the inline unit test above to validate the functionality of the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
As shown in the test cases above, the first test case returns True because all numbers in the list `[1, 2, 4, 10]` are below the threshold `100`. In the second test case, the list contains a number `[20]` that is greater than the threshold `5`, so the function returns `False`.