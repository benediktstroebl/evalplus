```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension with a condition that filters out elements that are not positive numbers. This creates a new list that only includes positive numbers from the original list. 

To test this, try calling the function with different lists and verify that it returns only positive numbers. For example:
```python
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected output: [5, 3, 2, 3, 9, 123, 1]
``` 

The expected output for each test is based on the markdown code block provided.