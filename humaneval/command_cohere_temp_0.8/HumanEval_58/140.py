```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` as arguments. It uses the `intersection` method to find the unique elements that appear in both lists, by using the `set()` function to remove any duplicate elements from `l1` and `l2`. Then it sorts the resulting list and returns it. 

This function fulfills the problem statement in the provided Markdown code block and ensures the correct output for the given test cases.