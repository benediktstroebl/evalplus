```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not discontinued]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
assert result1 == [0, 2, 3, 5, 5, 9, 123]

# Test case 2
discontinued = [2, 3, 3]
test_case2 = [5, 3, 5, 2, 3, discontinued, 9, 0, 123]
result2 = unique(test_case2)
assert result2 == [5, 3, 5, 9, 123]
```
The code defines a function unique that takes a list as an argument and returns a new list containing unique elements from the original list. This is does this use a set to keep track of the elements already encountered. The set of seen elements is then intersected with the original list to obtain the unique elements, which are then added back to the result list. The test cases demonstrate the using sample lists and assert that the result is correct.

I hope this helps you with your question!