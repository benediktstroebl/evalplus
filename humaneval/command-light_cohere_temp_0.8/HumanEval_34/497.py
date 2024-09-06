```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test case 1:
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
print("Test case 1 unique elements: ", result1)

# Test case 2:
test_case2 = [5, 2, 3, 7, 0, 9, 1, 8]
result2 = unique(test_case2)
print("Test case 2 unique elements: ", result2)
```
This script defines a function called unique that takes a list lst as input and returns a list of unique elements in the input list. It uses the simple strategy of creating a set seen and then iterating through the input list. The unique elements are then added to the result list if they are not already present in the set seen. The output of the expected test cases is displayed.