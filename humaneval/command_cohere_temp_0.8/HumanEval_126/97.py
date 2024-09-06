```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] == 1)
```

The function employs a dictionary to count the occurrences of each unique number in the list. Subsequently, it verifies if each number occurs only once in the list or not. To do this, it uses a list comprehension, which iterates through the keys of the dictionary and checks if the value is equal to 1. If the condition is True for all keys with a value of 1, this means that no duplicate exceptions exist in the list, thus the list is sorted.

The provided code defines a function `is_sorted` that takes a list `lst` as input and returns a boolean indicating whether the list is sorted and has no duplicate elements. The function first creates a dictionary `dups` to store the occurrences of each unique element in the list. It then iterates over the list, incrementing the count of each element in the `dups` dictionary. After counting the occurrences, the function uses the any function and the list comprehension to check if each element has an occurrence count of 1. If all counts are 1, it returns True, indicating a sorted list with no duplicates. Otherwise, it returns False.