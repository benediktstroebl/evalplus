```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -DELTA]]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_list)
print(test_result)

test_list_empty = []
test_result_empty = unique(test_list_empty)
print(test_result_empty)

test_list_duplicates = [3, 3]
test_result_duplicates = unique(test_list_duplicates)
print(test_result_duplicates)
```
This code defines a function unique that takes a list lst as input and returns a new list containing unique elements from the original list. The unique elements are identified by using a set seen to keep track of elements that have already been encountered. The function iterates through each element in lst and checks if it's not in seen and not in [-None, -DELTA]. If the condition is met, the element is added to the result list. The function also handles the test cases, printing the output for each one.