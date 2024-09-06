```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements from the list, and then uses the sort method to sort the elements.

The test case provided in the problem statement is to test the function unique on the list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`. The expected result is `[0, 2, 3, 5, 9, 123]`.

Here is a self-contained Python script that includes this function and a test case to verify the functionality:
```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l

# Test case
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

The test case unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) uses the function unique to return the sorted unique elements in the list. The expected result is `[0, 2, 3, 5, 9, 123]`, which is the sorted, unique elements of the list. When this test case is executed, the assert statement will return True if the comparison is true, or it will raise an AssertionError if the comparison is false. 

Therefore, this Python script solves the problem and provides test coverage to ensure that the code behaves as expected. 
If there are any questions or suggestions for other problems that I can help with, let me know!