```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all numbers in the list are below the threshold, and `below_threshold()` returns `True`. Otherwise, if any comparison is `False`, `all()` returns `False`, and `below_threshold()` returns `False`. The function works correctly for the given test cases, where it returns `True` for the first example and `False` for the second. 
To run this function simply call it with the list `l` and threshold `t` you want to test. For example:
```python
print(below_threshold([1, 2, 4, 10], 100)) # Output: True
print(below_threshold([1, 2, 4, 10], 5))  # Output: False
```