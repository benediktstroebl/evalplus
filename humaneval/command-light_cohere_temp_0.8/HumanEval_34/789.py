```python
def unique(l: list):
    return list(set(l))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [10, 2, 18, 100, 19]
assert sorted(unique(test_case2)) == [10, 2, 18, 100]

# Test case 3 (list of strings)
test_case3 = ["apple", "banana", "cherry", "date"]
assert sorted(unique(test_case3)) == ["apple", "banana", "cherry"]
```  This Python code defines a function named unique that takes a list as input and returns a new list containing only the unique elements from the original list. The code also provides three test cases to validate the behavior of the unique function:

Test Case 1: Asserts that the unique function correctly removes duplicate elements from the list [5, 3, 5, 2, 3, 3, 9, 0, 123], and returns the expected output [0, 2, 3, 5, 9, 123].

Test Case 2: Creates a new list [10, 2, 18, 100, 19] and asserts that passing it to the unique function removes duplicates and returns the expected output [10, 2, 18, 100].

Test Case 3: This test case validates the behavior of the unique function with a list of strings. It asserts that the expected output is the unique strings from the input list ["apple", "banana", "cherry", "date"], which are ["apple", "banana", "cherry"].