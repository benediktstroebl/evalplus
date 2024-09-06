Here is a Python script with a self-contained function that solves the problem of returning unique elements in a list:
```python
import itertools
def unique(lst):
    return list(set(itertools.chain(lst)))
```
The function `unique` takes a list `lst` as input and returns a list of unique elements from the input list. 

This function utilizes the `set()` function from the `itertools` module and `itertools.chain()` function to create an unordered set from the list, and then `list()` function to convert the set back to a list. 

This solution is self-contained and does not require any external functions or modules.