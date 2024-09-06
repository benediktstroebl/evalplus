```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example usage of the function that tests its functionality:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This example tests the function with two different inputs against the given examples in the prompt. The function returns `True` for the first example test since all the numbers in the list `[1, 2, 4, 10]` are below the threshold value of `100`. In the second test, the function returns `False` since the list contains a number `20` that is above the threshold value of `5`.