```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, indicating that all numbers in the list are below the threshold, otherwise `False`.  This behavior is appropriately illustrated in the docstring:
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
``` 
This will return `True` if the list contains all numbers less than the threshold, and `False` otherwise. 
The tests explicitly illustrate the behavior of the function with different inputs. 
If the problem statement requires a markdown code block, you can embed this code within that block with triple backticks ````python ``. 
Please let me know if you have any other questions! 
I'm here to help.