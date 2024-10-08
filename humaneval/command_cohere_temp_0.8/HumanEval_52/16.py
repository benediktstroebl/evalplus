```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
list_ = [1, 2, 4, 10]
threshold = 100

print(below_threshold(list_, threshold))
```
This will output:
```
True
```

And here is another example where the list contains one element that is not below the threshold:
```python
list_ = [1, 20, 4, 10]
threshold = 5

print(below_threshold(list_, threshold))
```
This will output:
```
False
```