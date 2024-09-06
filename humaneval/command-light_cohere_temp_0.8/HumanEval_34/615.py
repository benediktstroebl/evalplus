```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test 2
assert unique([]) == []

# Test 3
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
``` 
This Python function unique is designed to take a list as input and return a list containing only the unique elements from that list. The set seen is initialized to keep track of unique elements, and a new list is built to include only elements that are not present in the set seen yet. The function iterates through each element in the list and checks if it is not in the set seen. If it's not, the element is added to the list and the set seen is updated.