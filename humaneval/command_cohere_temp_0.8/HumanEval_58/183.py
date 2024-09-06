```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` retrieves the common elements between the two lists. Finally, `sorted` is applied to organize the result in a sorted manner. The output of this function is the list of common elements between the two input lists, removed of duplicates and sorted. 

To handle the tests, there should be two lists provided in the parenthesis of the `common` function and the resulting output list should be displayed on the next line. For example:
```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))

# Example 1
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))

# Example 2
print(common([5, 3, 2, 8], [3, 2]))
```

This will output:
```bash
[1, 5, 653]
[2, 3]
``` 
Which is the expected result for the given inputs in the example block. 
The function should be able to handle any list inputs to return the common elements between them. 
If you would like more examples tested or would like to verify this solution further, let me know!