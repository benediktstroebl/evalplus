```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test the function with some examples
assert(unique([5, 3, 5, 2, 3, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123])

```  This code defines a function `unique` that takes a list as an argument and returns a new list containing only the unique elements from the input list. The function uses a unique() function and a set to keep track of unique elements. It then iterates through elements from the list, and adds elements to the set if they are not present in the set. After processing the unique elements element in the list, the function returns the new list containing unique elements.