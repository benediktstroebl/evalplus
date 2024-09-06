```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in l. It removes duplicate elements employing the set method and sorts the values using the sort method. 

To test this function, you can invoke it with a list of integers and compare the result with the expected output. 

For example:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected_result = [0, 2, 3, 5, 9, 123]
result = unique(test_list)
print(result)  # Expected output: [0, 2, 3, 5, 9, 123]
print(result == expected_result)  # Expected output: True
```

This would yield the following output:
```
[0, 2, 3, 5, 9, 123]
True
``` 

The first line shows the output of the unique function when applied to the test_list. The second line proves the equivalence of the result and expected_result. 

This indicates that the unique function is operating correctly as it successfully sorts and removes duplicates from the input list.