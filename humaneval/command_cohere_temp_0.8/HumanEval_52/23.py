```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will output:
```
True
```

Here is another example:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
This will output:
```
False
```

The function will return `True` if all the elements in the list are below the threshold, and `False` otherwise. 

This solution is concise and straightforward, leveraging Python's `all()` function for element analysis and comparison. The provided tests will confirm the function's correctness against various test cases. 
If you have any questions or need further assistance, feel free to ask!