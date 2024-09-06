```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

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
Which will output:
```
False
```

This new implementation passes the given tests and is more intuitive and simpler than the original implementation.