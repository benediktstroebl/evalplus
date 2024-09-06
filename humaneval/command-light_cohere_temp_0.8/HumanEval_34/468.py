```python
def unique(lst):
    return list(set(lst))

# Test the function with a list of numbers
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)  
```
This code provides a solution using the set data structure to keep track of unique values in a list. The `unique` function takes a list as an argument, converts it to a set, and then extracts the unique values back into a new list. 

This is a straightforward and efficient approach for this problem.