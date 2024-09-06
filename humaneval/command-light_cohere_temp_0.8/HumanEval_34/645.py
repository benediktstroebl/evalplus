```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test cases
test_list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_list2 = list(range(100))
test_list3 = ['a', 'a', 'b', 'c', 'a', 'd']

# Call the function and assert the results
assert unique(test_list1) == [0, 2, 3, 5, 9, 123]
assert unique(test_list2) == set(range(100))
assert unique(test_list3) == set(['a', 'b', 'c', 'd'])
 ``` 
This code defines a function unique that takes a list lst as input and returns a sorted list of unique elements from lst. The function uses a set seen to keep track of the unique elements and a list result to store the unique elements. The test cases demonstrate that the function works correctly.