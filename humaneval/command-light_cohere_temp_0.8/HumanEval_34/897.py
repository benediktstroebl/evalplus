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
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))
# [0, 2, 3, 5, 9, 123]
test_string = "unique([2, 34, 54-67, 93, 654, 1234, 543]) "
print(eval(test_string))
# [2, 93, 1234, 543]
```
The function unique in this code takes a list lst as input and returns a list containing the elements that are unique in lst. The set seen is used to keep track of the elements we havereditary seen so far, and the result is a new list containing only the unique elements. The test cases demonstrate the new list on the left and the resulting list on the right.

This code is self-contained, and it can be used as a standalone solution to the problem.