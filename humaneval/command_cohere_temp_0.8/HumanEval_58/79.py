```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters. It uses the `intersection` method to find the unique elements common in both lists, then sorts these elements using the `sorted` function, and returns the final result. 

This function meets the problem requirements specified in the original markdown code block and should successfully pass the tests provided.