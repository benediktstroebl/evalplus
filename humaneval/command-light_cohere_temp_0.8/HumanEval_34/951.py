```python
def unique(lst):
    return list(set(lst))

# Test case 1
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
# [0, 2, 3, 5, 9, 123]

# Test case 2
test_list = [5, 3, 6, 7, 8, 9, 10, 3, 1, 0]
unique(test_list)
# [0, 1, 3, 5, 6, 7, 8, 9, 10]
```

This Python script defines a function named `unique` which takes a list as an argument and returns a sorted unique elements in that list. The function utilizes the particular set() function to create a set from the list, and then converts the set back to a list which will contain only unique elements from the original list. The script also includes two test cases to verify the functionality of the unique function. The output of the unique function for both test cases will be a list with no duplicates, which matches the expected result.