```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and checks if each item is less than the input threshold `t`. 

Here is an example usage of the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
```
True
```

And here is another example usage of the function:
```python
print(below_threshold([1, 20, 4, 10], 5))
```
```
False
```

These examples demonstrate that the function returns `True` if all the numbers in the list are below the threshold, and `False` otherwise.  This should help you to achieve the desired result for the problem you posted. Let me know if you need anything else!