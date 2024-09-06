```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the less-than (`<`) operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`.  The bool return type of the function is used to indicate the truthfulness of the result. The function shows an example usage upon invocation to validate the accuracy of the comparison. 

Here is an example usage of the function to test its correctness:
```python
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))  # Output: False
```

This demonstrates the use of the `below_threshold()` function with two examples. In the first example, the list contains numbers that are all less than the threshold value of 100, so the function returns `True`. In the second example, the list contains a number (20) that is not less than the threshold value of 5, so the function returns `False`. 

This function provides a straightforward and concise way to determine whether a list of numbers is below a given threshold and can be easily incorporated into larger code bases.