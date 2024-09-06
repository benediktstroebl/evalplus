```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, cnt in dups.items():
        if cnt > 1:
            return False
    return True
```

The function employs a simple algorithm that takes a list of numbers and determines whether they are sorted and if there are any duplicate numbers. First, it generates a dictionary, `dups`, that stores the integers from the list and their corresponding counts. If the count of any number is more than one, this indicates duplicates, and the list is not sorted, so the function returns False. If no duplicates are found, it returns True.

This algorithm boasts a time complexity of O(n), where 'n' is the number of elements in the input list, making it efficient for most applications.