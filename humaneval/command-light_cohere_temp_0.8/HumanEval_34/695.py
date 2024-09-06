```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not Infinity]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test case 1:", unique(test_case1))
assert all(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
infinity = float("inf")
test_case2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Test case 2:", unique(test_case2))
assert unique(test_case2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Test case 3 (lists with same item)
test_case3 = [1, 1]
print("Test case 3:", unique(test_case3))
assert unique(test_case3) == [1]
``` 
This script defines a function called unique which takes a list as input and returns a list containing unique elements from that list. The test cases verify the essential the using test cases, the output of the unique function is compared with the expected results, and the test passes if the output is correct.