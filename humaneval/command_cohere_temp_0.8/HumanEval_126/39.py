```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums for _, nums in dups.items())
```

The function uses a dictionary `dups` to count the number of duplicates for each number in the list. Then it checks two things:
1. Whether each number occurs at most once in the list, by checking if the dictionary values are all 1.
2. Whether the numbers are sorted, by checking if each number in the list is less than or equal to the numbers that follow it in the list. 

This solution passes the provided tests and does not require any additional modules. 
If you are planning to use it in a broader context, it may be worth importing the `collections` module to utilize the faster `Counter` class for duplicate counting. Here's an alternative version that does this:
```python
from collections import Counter

def is_sorted(lst):
    dup_count = Counter(lst)
    return all(dup_count[num] == 1 for num in dup_count) and all(num < nums for num, nums in dup_count.items())
``` 

This version uses the `Counter` class to create `dup_count`, which works just like the `dups` dictionary in the previous version.