```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example usage of the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will return:
```
True
```
The function will return `True` because all numbers in the list `[1, 2, 4, 10]` are below the threshold value of `100`.

Here is another example usage of the function:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
This will return:
```
False
```
The function will return `False` because one or more numbers in the list `[1, 20, 4, 10]` are not below the threshold value of `5`. 
The function, when applied to the provided test cases, correctly returns `True` for the first test case and `False` for the second test case, indicating that the function correctly solves the problem.