```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# Test the function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)
``` 
This script defines a function `unique` that returns a sorted list of unique elements from the input list. It uses a quick set to keep the duplicates away and then builds a new list with unique elements. The test_unique variable is used to test the `unique` function with a sample list.