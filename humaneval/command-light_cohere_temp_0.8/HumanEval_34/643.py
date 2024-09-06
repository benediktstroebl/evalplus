```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Test cases
test_cases = [ [5, 3, 5, 2, 3, 3, 9, 0, 123], [1, 2, 3, 4, 5, 6], [True, 'a', 'b', 'c']]

for test_case in test_cases:
    actual = unique(test_case)
    assert actual == [0, 2, 3, 5, 9, 123]
``` 
This code defines a function called unique that takes in a list and creates a set of its unique elements. It then creates a unique elements in the set and adds them to a list, which is returned as the result. The test cases demonstrate the unique function by passing various lists to it and asserting that the returned list of unique elements matches the expected result.