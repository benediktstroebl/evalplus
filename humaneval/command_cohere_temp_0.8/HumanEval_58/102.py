```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2`, as parameters. It uses the `intersection` method to find the unique elements that appear in both lists, by utilizing the appropriate setter (`set`) to eliminate duplicate elements, and returns these elements sorted in ascending order. 

This solution is efficient with a time complexity of O(min(len(l1), len(l2))). It utilizes the inherent efficiency of the `intersection` method and the `set` data structure to perform the operations in linear time. 

Additionally, this solution is quite concise, utilizing Python's powerful syntax and built-in methods to solve the problem with just a few lines of code. 

Note: The `common` function assumes that the input lists `l1` and `l2` are not empty. If this is not the case, the function will raise an error. If empty lists are a potential input, consider adding preprocessing steps or error handling to address this possibility.