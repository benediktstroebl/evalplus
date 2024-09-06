Here's the self-contained Python function that solves the problem of getting unique elements in a list:

```python
def unique(lst):
    return list(set(lst))
```

This function takes a list `lst` as input and returns a new list with unique elements from the original list.

We use the `set()` function along with the `list()` function to convert the input list into a set, which inherently contains unique values. Then, we convert the list from the set back into a list using the `list()` function. 

This approach ensures that duplicate elements are automatically eliminated, resulting in a list with unique elements. 

This function is self-contained and does not require any external functions or variables. It is a easy to use and understand, making it a clean and effective solution for this problem.