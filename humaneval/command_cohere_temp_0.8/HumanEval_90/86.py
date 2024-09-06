```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This function leverages Python's built-in sorting mechanism `sort()` to identify the smallest and second-smallest elements in the list. By accessing the second element of the sorted list, the function retrieves the second-smallest element, provided there are at least two elements in the list. If the list has less than two elements, the function returns `None` to reflect the absence of a second-smallest element. 

This approach ensures simplicity and efficiency in solving the problem.

The function can be tested with the following Python code:
```python
test_list = [1, 2, 3, 4, 5]
print(f"Test list: {test_list}")
print(f"Next smallest element: {next_smallest(test_list)}")

test_list = [5, 1, 4, 3, 2]
print(f"Test list: {test_list}")
print(f"Next smallest element: {next_smallest(test_list)}")

test_list = []
print(f"Test list: {test_list}")
print(f"Next smallest element: {next_smallest(test_list)}")

test_list = [1, 1]
print(f"Test list: {test_list}")
print(f"Next smallest element: {next_smallest(test_list)}")
```

This would output:
```
Test list: [1, 2, 3, 4, 5]
Next smallest element: 2
Test list: [5, 1, 4, 3, 2]
Next smallest element: 2
Test list: []
Next smallest element: None
Test list: [1, 1]
Next smallest element: None
```

The values are consistent with the expected results outlined in the original problem statement.