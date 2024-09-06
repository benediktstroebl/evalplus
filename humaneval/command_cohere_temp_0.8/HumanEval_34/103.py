```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function named unique which takes a list l as input. Inside the function, a set called seen is used to keep track of unique elements encountered while iterating through the input list. The function employs a list comprehension to filter elements that are not already present in the seen set and safely adds them to the seen set. Finally, it returns the sorted result. 

The function effectively eliminates duplicates, guaranteeing that each element is only included in the output once, and sorts the result list. 

The problem statement includes a docstring with expected test cases, and the Python script's function uniquely handles these cases.

For the test case of the list containing [5, 3, 5, 2, 3, 3, 9, 0, 123], the expected output is [0, 2, 3, 5, 9, 123], and the function uniquely() returns the correct result. 

This Python function is a self-contained solution to the problem statement and complies with the specified docstring tests.