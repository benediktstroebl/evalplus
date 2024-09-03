Here is a self-contained Python script that solves the problem of finding the largest and smallest integers in a list of integers:
```python
def largest_smallest_integers(lst):
    if len(lst) == 0:
        return (None, None)
        
    max_num = max(lst)
    min_num = min(lst)
    
    if max_num < 0:
        max_num = -max_num  # Swap to ensure positive

    return (max_num, min_num)

# Test cases
test_cases = [
    [2, 4, 1, 3, 5, 7],
    [],
    [0],
    [-200, 200],
]

for test_case in test_cases:
    result = largest_smallest_integers(test_case)
    print("Test case:", test_case)
    print("Result:", result)
    print()
```

This script defines a function `largest_smallest_integers` that takes a list of integers as input and returns a tuple containing the largest and smallest integers. The script then provides a test cases, and the function is executed for each case. 

Note that the function is designed to handle the edge case where the input list is empty, and it returns `None` for both elements in such cases.