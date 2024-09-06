```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` iterates over the list and filters elements that are greater than zero, returning the final list that contains only positive numbers. 

Here is an example of how to use the code:
```python
print(get_positive([-1, 2, -4, 5, 6])) # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [5, 3, 2, 3, 9, 123, 1]
```

This will output the following:
```
[2, 5, 6]
[5, 3, 2, 3, 9, 123, 1]
```

The code directly translates the given Markdown code block into a working Python script that achieves the desired result of filtering out only the positive numbers from the list.