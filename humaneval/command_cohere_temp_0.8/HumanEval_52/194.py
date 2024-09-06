```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compares each element with the threshold value `t`. 

Here is an example usage of the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This example demonstrates the function's behavior as described in the problem statement. The function returns `True` if all numbers in the list are below the threshold, and `False` otherwise. 
The exact output aligns with the previously provided examples, reinforcing the function's correct implementation.