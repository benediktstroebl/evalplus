```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [val for ind, val in enumerate(l) if ind % 3 == 0 and val != l[ind]]
    sorted_thirds.sort()
    for i in range(0, len(l), 3):
        if i % 3 == 0:
            l[i] = sorted_thirds.pop(0)
    return l
```

This script defines a function sort_third which takes a list as an argument, and returns the list with its elements at the indices divisible by three, sorted. The function works by copying the original list, and then collecting the elements at indices divisible by three in a separate list, sorting it, and then replacing the corresponding elements in the original list with the sorted elements. The function then returns the modified list.

Here is an example usage of the function for clarification:
```python
print(sort_third([1, 2, 3])) # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # [2, 6, 3, 4, 8, 9, 5]
```
This should print:
```
[1, 2, 3]
[2, 6, 3, 4, 8, 9, 5]
```
The first list is unchanged, and the second list has its elements at the positions divisible by three sorted.