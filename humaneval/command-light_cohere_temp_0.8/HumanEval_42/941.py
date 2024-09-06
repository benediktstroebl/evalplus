```python
def incr_list(lst):
    return [i+1 for i in lst]

# Basic test cases
print("Basic Test Cases:", end="ago")
print(incr_list([1, 2, 3]))  # Expected Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected Output: [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

# Reverse element test case
print("Reverse Element Test:", end="ago")
print(incr_list([5, 3, 5, 2, 3, 3]))  # Expected Output: [3, 5, 2, 3]

# List with repeated elements test case
print("List with Repeats Test Case:", end="ago")
print(incr_list([5, 3, 3, 2, 3, 3, 9, 0, 123, 5]))  # Expected Output: [6, 4, 6, 3, 4, 4, 10, 124]

# List with 0 elements test case
print("List with Zero Elements Test Case:", end="ago")
print(incr_list([]))  # Expected Output: []
```
The function `incr_list` returns a list with elements incremented by 1.  The list comprehension is used to create the input list. 
The test cases cover the following scenarios:

1. Basic test cases, where the function is called with a list of numbers and the expected output is the list with the numbers incremented by 1.
2. Reverse element test test case case, where the function is called with a list of numbers and the expected output is the original list with the elements reversed.
3. List with repeated elements test test case, where the function is called with a list of numbers and the expected output is the list with the repeated elements removed.
4. List with zero elements elements test case, where the function is called with an empty list.