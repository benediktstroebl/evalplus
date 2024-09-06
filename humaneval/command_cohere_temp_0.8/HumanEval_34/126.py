```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements from the list, and then uses the sort function to sort the unique elements. 

To ensure the function works as expected, let's test it with some examples. 

```python
# Test 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123] 

# Test 2
assert unique([1, 1, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5] 

# Test 3
assert unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
``` 

The assertions should pass, confirming that the function unique correctly sorts and returns unique elements from the input list. 

Feel free to ask any questions or provide additional information for more tailored assistance!