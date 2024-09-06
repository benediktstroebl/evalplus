```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return len(lst) == len(set(lst)) and all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

The function uses two nested conditions to check if the list is both sorted and has no duplicates, returning false if either condition is not met. The first condition checks if the list is sorted by verifying that each element is no greater than the next, and the second condition checks if there are no duplicates by verifying that each element is unique. 

The overall time complexity of this solution is O(n log n), where 'n' represents the size of the input list. This is because the algorithm requires checking every item in the list against all previous items in the list to ensure sorting and uniqueness. 

This solution is applicable to the problem, effectively addressing the conditions outlined. It achieves this without relying on additional modules, ensuring adaptability and portability.