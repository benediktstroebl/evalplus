```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements present in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This approach ensures that each element is included in the output only once, and the output is sorted accordingly. Let's verify the results using an example:
```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

Output:
```
[1, 5, 653]
[2, 3]
```

The output is consistent with the given test cases from the original prompt. 

This function is also efficient; the time complexity is O(min(len(l1), len(l2)) * log(max(len(l1), len(l2))). This is because the intersection is calculated in O(min(len(l1), len(l2)) ) and sorting in O(max(len(l1), len(l2)) ).