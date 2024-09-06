```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element against the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))     # Output: True
print(below_threshold([1, 20, 4, 10], 5))    # Output: False
```
This will return `True` because all numbers in the first example are below the threshold value of 100, while the opposite is true for the second example with the threshold set to 5.