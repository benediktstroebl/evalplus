```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each item in the input list `l` and compare each item with the threshold value `t`. 

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

This would return `True` because all numbers in the first example list `[1, 2, 4, 10]` are less than the threshold value of `100`, and return `False` in the second case because the list includes a number `[20]` that is greater than the threshold value of `5`. 

If you need to customize the functionality or handle more edge cases, I can provide additional assistance. Let me know if I can help further with the problem or any other coding challenges!