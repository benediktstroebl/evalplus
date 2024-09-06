```python
def is_sorted(lst):
    # Count the unique elements and sort the list
    unique, sorted_list = set(lst), sorted(lst)
   
    # If unique elements are more than one and the list is not sorted, return False
    if len(unique) > 1 and sorted_list != lst:
        return False
    # Return True if the list is sorted or has only 1 unique element
    return True
```

This function uses two main steps:
1. It transforms the input list into a set to count the number of unique elements and sorts the list in the same operation.
2. It then simply checks if the set of unique elements is more than one and if the sorted list is different from the original list to determine if it's sorted.

This algorithm should provide a correct solution to the problem as per the given test cases in the markdown code block. 

Feel free to let me know if you would like me to explain any of the steps I took in more detail or provide any further optimizations for this solution. Let me know if you'd like to go through any other problems too!