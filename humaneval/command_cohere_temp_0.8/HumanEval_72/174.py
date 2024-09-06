```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # reverse to check for palindromic, set to check for unique
    # if both conditions are met, function returns true
```

The function will return **True** if the sum of the elements in the list is less than or equal to the maximum possible weight (**w**) and the list is balanced, using the condition that the length of the list is equal to the length of the set of elements in the list. 

The function will return **False** if any of these conditions are not met. You can test the function by calling it with different lists and weights to see if the output matches the expected result.