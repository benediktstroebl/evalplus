```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
The result of this comparison is either True or False, and since the `all` function returns True only if all its inputs are True, thereby indicating that all elements in the list are below the threshold, the result of the `below_threshold` function is True.

Here is an example usage of the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This example usage shows that the function returns True for the first example when all elements in the list are less than the threshold value of 100, and returns False for the second example when the list contains elements greater than the threshold value of 5.