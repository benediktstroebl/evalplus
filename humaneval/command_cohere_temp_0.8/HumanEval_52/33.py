```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and checks if each element is less than the input threshold `t`. 

Here is an example usage of the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
```
This will give an output of:
```
True
```

Here is another example usage of the function:
```python
print(below_threshold([1, 2, 4, 10], 5))
```
This will give an output of:
```
False
```