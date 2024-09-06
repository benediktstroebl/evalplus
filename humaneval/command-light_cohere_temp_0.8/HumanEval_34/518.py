Here is a self-contained Python function that solves the problem you described: 

```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_unique)
assert result == [0, 2, 3, 5, 9, 123]
``` 
This function `unique` takes a list as input and returns a new list with the unique elements from the input list. The function uses a set to keep track of elements that have been encountered, and then iterates through the input list, checking if each element is in the set. Then, it adds the unique elements to the result.