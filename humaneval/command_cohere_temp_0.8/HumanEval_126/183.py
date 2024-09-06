```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return len(set(lst)) == len(lst) and all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple algorithm that checks if there are any duplicates in the list and if so, whether there are more than one occurrence of the same duplicate. Then it verifies whether the list is sorted without explicitly comparing every pair of elements. The function returns True if the list is sorted and has only unique elements, and False otherwise.  This algorithm is efficient and has a time complexity of O(n), where n is the length of the input list.