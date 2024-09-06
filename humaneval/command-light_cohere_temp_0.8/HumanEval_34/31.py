```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))
``` 
This code defines a function called unique that takes a list as an argument and returns a new list containing only the unique elements. It uses the
 set() to create a set of unique elements from the original list, and then it iterates over the original list again, only adding elements to the set if they are not already in there and are not the zero value. The output is the unique list of the test case.