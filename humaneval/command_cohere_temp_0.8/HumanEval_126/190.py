```python
def is_sorted(lst):
    lst.sort()
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list, then it iterates through the sorted list, using a set to keep track of the unique values as it does so. If the set contains more than one instance of a value, the function returns false, indicating that the list is not sorted. If the set contains exactly one instance of each value in the list, the function returns true, indicating that the list is sorted. 

The `seen` set allows the function to efficiently check for duplicates in the list, without having to resort to more expensive operations like `len(set(list))`. 

This solution is efficient and uses a time complexity of O(n log n) due to the sort algorithm and then O(n) for iteration through the list. 

This approach allows the function to solve the problem by only needing to iterate through the list once, making it an efficient and effective solution.