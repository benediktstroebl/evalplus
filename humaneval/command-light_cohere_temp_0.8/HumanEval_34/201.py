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
test_case_1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case_2 = [2, 18, 18, 1, 19, 4, 5]
test_case_3 = ['a', 'b', 'c', 'd', 'e', 'f']

# Test function
results = unique(test_case_1)
print("Test case 1 results:", results)
results = unique(test_case_2)
print("Test case 2 results:", results)
results = unique(test_case_3)
print("Test case 3 results:", results)
```
This script defines a function `unique` that takes a list as an argument and returns a new list with unique elements from the input list. The function uses a set to keep track of elements already encountered, and a new list is built by iterating through the input list. The unique elements are then appended to the result list. The test cases demonstrate the function usage by passing different lists and printing the resulting unique elements.