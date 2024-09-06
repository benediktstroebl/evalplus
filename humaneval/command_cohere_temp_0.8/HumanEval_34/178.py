```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements from the list, and then uses the sort method to sort the unique elements. 

To ensure the function adheres to the problem statement, let's test the function against the given example:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected_result = [0, 2, 3, 5, 9, 123]

assert unique(test_list) == expected_result
```

The test passes, confirming that the function unique solves the problem as stated.