```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The function takes a string as input and returns the sum of the upper characters' ASCII codes. It utilizes the `filter` method with a `str.isdigit` check to extract all digit characters from the string. These filtered characters are then converted to integers using `map` and summed using the `sum` function to provide the final result.

This approach allows the function to efficiently calculate the sum of digit characters in the provided string.