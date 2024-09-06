```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test 1
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))
# [0, 2, 3, 5, 9, 123]

# Test 2
test_list2 = [6, 7, 8, 9, 10, 3, 2, 4, 5]
print(unique(test_list2))
# [2, 3, 4, 5, 6, 7, 8, 9]
``` 
This script defines a function unique that takes a list as input and returns a list containing the unique elements in that list. It uses a unique elements approach to the list, and for each new element, it checks if it's already in the set seen.