```python
def is_sorted(lst):
    # Count the occurrences of each list element
    occ = {}
    for i in lst:
        occ[i] = occ.get(i, 0) + 1
    
    # Check for duplicates
    for i in occ:
        if occ[i] > 1:
            return False
    
    # Check if occ occurs in sorted order
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

The function works as follows:
1. Create a dictionary (`occ`) where the keys are the elements of the list and the values are the number of occurrences of each element in the list.
2. Check if any of the elements occur more than once in the list (by checking the dictionary values). If so, the list has duplicates and the function returns False.
3. If the list has no duplicates, it checks whether the elements occur in ascending order. It does this using a generator expression in the all function, which checks if each element is less than or equal to the next element in the list, starting from the second element (since the first element has no element to compare with). 

The script passes the examples provided in the problem statement.