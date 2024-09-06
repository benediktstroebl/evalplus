```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l] + [n]
    return result

# Test cases
test_incr_list = [
    [
        [1, 2, 3], 
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ]
]

test_case_results = {}
for test_case in test_incr_list:
    test_case_results[test_case] = incr_list(test_case)

# Print the results of all test cases
for key, value in test_case_results.print(result)
```
The provided code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The function achieves this goal using a simple list comprehension with a loop that adds 1 to each element in the input list, followed by adding the length of the original list. 

This code effectively demonstrates the ability to build functions that operate on data structures and produce new values based on the input provided.