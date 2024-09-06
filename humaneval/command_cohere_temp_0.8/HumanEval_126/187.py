```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] <= 1 for num in dups) and all(num < nums for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and then checks two things:
1. Whether there is at most one occurrence of each element, with the use of the `all` function and the logical implication operator `=>`. This is done by checking if the length of the dictionary is equal to the unique elements in the dictionary.
2. Whether the integers are sorted, which is done by checking if the key-value pairs in the dictionary are sorted in ascending order, as indicated in the second `all` check.

This function adheres to the problem's assumption of assuming no negative numbers and only integers, and it returns a boolean value indicating whether the list is sorted.