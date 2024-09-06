```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Test the function with a sample list
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)  
```  This script defines a function unique that takes a list as an argument and returns a new list with unique elements from the original list. The function uses the use of the set function to filter out duplicate elements and then apply the sorted function to create a new sorted list with unique elements. The script also includes a test_unique variable that is used to test the unique function with a sample list. The expected output is [0, 2, 3, 5, 9, 123].  This script demonstrates the implementation of a function that solves the problem of returning unique elements from a list in a self-contained manner.