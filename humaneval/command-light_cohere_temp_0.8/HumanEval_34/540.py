```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))
# [0, 2, 3, 5, 9, 123]

test_string = " # Comment"
print(unique(test_string.strip())
# []

test_list = [1, "One", 2, "Two", 3, "Three"]
print(unique(test_list))
# [['One', 'Two', 'Three']]
``` 
This code defines a function called `unique` which returns a list containing the unique elements of the input list. The function uses a set to keep track of elements that have been encountered before, and it iterates through the input list, adding elements to the set if they are not already present. The unique elements of then added to the result list.