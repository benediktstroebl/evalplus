```python
def sort_third(l):
    l_copy = l.copy()
    return [(val if i % 3 != 0 else sorted(l_copy)[i // 3]) for i, val in enumerate(l)]
```

This script defines a function `sort_third` which takes in a list and returns a list in which every index not divisible by three is unchanged, while the elements at divisible-by-three indices are sorted. The behavior is achieved through generating a new list with the desired properties using list comprehension and copying the original list. Would you like to know more about the code or problem?