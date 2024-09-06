```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`.  If all elements are less than `t`, the function returns `True`, otherwise it returns `False`.  This fulfills the problem statement requirements. 
This function works correctly for the given test cases:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
``` 
The first example returns True because all numbers in the list `[1, 2, 4, 10]` are below the threshold value of `100`. In the second example, the result is False because not all numbers in the list are below the threshold value of 5.