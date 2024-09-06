```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0,]] + seen

# Test cases 

# [unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
#   [0, 2, 3, 5, 9, 123]

# Longer list with duplicates 

unique([1, 2, 3, 4, 5, 6, 7, 8, 9])
#   [1, 2, 3, 4, 5, 6, 7, 8, 9]

#mixed list 

unique([10, 10: , 5, 6, 7, 8, 9])
#   [10, 10:", 5, 6, 7, 8, 9]
``` 
The unique function uses the set data structure to quickly filter out duplicates, then adds the remaining elements to a new list. The test cases demonstrate its function with various inputs and the expected output.