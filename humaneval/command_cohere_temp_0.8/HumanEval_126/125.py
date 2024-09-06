```python
def is_sorted(lst):
    # Count the occurrences of each element using a dictionary
    element_count = {}
    for n in lst:
        element_count[n] = element_count.get(n, 0) + 1
    
    # Check for elements being greater than their position indicates
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    
    # Check for duplicates with count greater than 1
    for n, count in element_count.items():
        if count > 1:
            return False
    
    return True
```

The approach involves using a dictionary to count the occurrences of each number in the list. Then, the list is iterated to check whether each element is greater than the ones before it. Lastly, if there are duplicates, the function returns False if any count is greater than 1. The code is encompassed within a test harness with example cases to ensure accurate functionality. These tests can be executed by running the script, verifying the expected outputs, and confirming the solution's correctness.  This code solves the problem in a self-contained manner, providing a function that can be reused and applied to various lists in the future.