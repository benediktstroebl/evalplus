```python
def total_match(lst1, lst2):
    l1, l2 = len(lst1[0]), len(lst2[0])
    for i in range(1, min(len(lst1), len(lst2))):
        if l1 + l2 != len(lst2[i]) + len(lst1[i]):
            return lst1 if l1 <= l2 else lst2
    return lst1 if l1 <= l2 else lst2
```

The solution utilizes the fact that the strings in both lists are assumed to be non-empty. Thus, if the sum of the char count of strings in `lst1` is greater than or equal to the sum of the char count of strings in `lst2`, it is guaranteed that the result will be `lst1`. The function iterates through the lists, but the iteration is terminated after the shorter of the two lists, since the longer list, if present, will have a corresponding string in the shorter list, and the char count of that string will contribute to the total char count of the longer list. 

The stopping condition also ensures that if the number of elements in either list is insufficient to result in a decisive result, a fallback decision is made based on the initian comparison of the char counts of the first elements of each list. 

This algorithm has a time complexity of O(n) where `n = min(len(lst1), len(lst2))`.