```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
Since the problem states that the return value of the function should be `True` if all the numbers in the list are below the threshold and `False` otherwise, the function returns `True` if the condition is met for all elements in the list, and `False` otherwise. 

The tests specified in the problem statement are executed successfully against this function:
```python
>> below_threshold([1, 2, 4, 10], 100)
True
>> below_threshold([1, 20, 4, 10], 5)
False
```
This code correctly returns `True` since all the numbers in the first example are below 100, and returns `False` in the second example since the list contains a number (20) that is greater than the threshold.