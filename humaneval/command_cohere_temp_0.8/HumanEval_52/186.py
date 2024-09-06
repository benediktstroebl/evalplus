```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and checks if each element is less than the given threshold `t`. 

The `all()` function returns `True` if all elements are less than the threshold, meaning that the result of the function `below_threshold` will be `True`. Otherwise, `all()` will return `False`, and so will the function. 

This solution corresponds to the specification of the problem as it appears in the prompt. Let’s verify this by running some tests:
```python
# Test 1: List with one element below the threshold
>>> below_threshold([1, 20, 4, 10], 5)
False

# Test 2: List with all elements below the threshold
>>> below_threshold([1, 2, 4, 10], 100)
True

# Test 3: Empty list
>>> below_threshold([], 100)
True
```
As expected, the function `below_threshold` returns `True` for Test 2 and `False` for Test 1. Test 3 shows that the function correctly handles an empty list as well.