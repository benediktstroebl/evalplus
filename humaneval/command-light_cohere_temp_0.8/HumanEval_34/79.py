```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x, x)
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_list)
print("Test 1:", test_result)

test_list2 = [1, 2, 3, 4, 5, 6]
test_result2 = unique(test_list2)
print("Test 2:", test_result2)
```
The function unique takes an input list and returns a new list with unique elements. It uses a unique elements to sort the list and keeps track of elements that have already been seen using a set. The final result is a new list containing the unique elements. The test cases demonstrate the unique's functionality by passing two test lists and printing the results.