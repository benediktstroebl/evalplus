```python
def below_threshold(lst, t):
    return all(x < t for x in lst)

# Example function call
below_threshold([1, 20, 4, 10], 5)  # Output: False

# Test case with elements above threshold
below_threshold([3, 7, 5], 3)  # Output: True
```
This code provides a function called below_threshold that checks whether all elements in a given list lst are less than a given threshold t. The function uses the static list comprehension to iterate through the list and verify each element against the threshold. The function returns True if all elements are below the threshold, and False otherwise.