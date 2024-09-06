```python
def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum`, which takes a list of strings as input. Here's what the function does:
1. Uses a list comprehension to filter out strings from the input list that have odd lengths. Elements with even lengths are retained, as implied by the condition `len(e) % 2 == 0`.
2. Sorts the list of even-length strings using a two-level sorting key. At the first level, elements are compared by their length, with shorter elements coming first (`-len(x)`). If two elements have the same length, they are compared alphabetically at the second level (`x`).
3. Finally, the function returns the sorted list of even-length strings.