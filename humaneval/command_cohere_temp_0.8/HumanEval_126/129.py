```python
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) and len(set(lst)) == len(lst)
```

The function leverages two conditions to determine list sorting:
1. **All elements are unique**: We verify this using the `set` function, which converts the list to a set, which has unique elements by definition. Then, we check if the length of the set is equal to the length of the initial list. If they are the same, all elements are unique.
2. **Sorted order**: We use a generating loop to compare each element with the next one in the list. If all comparisons return true, the list is sorted.

The above approach results in a time complexity of `O(n^2)`, due to the loop traversing the entire list for comparisons. It yields a space complexity of `O(1)` as it only utilizes a single loop.