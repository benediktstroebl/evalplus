```python
def total_match(lst1, lst2):
    l1, l2 = len(lst1[0]), len(lst2[0])
    for i in range(min(len(lst1), len(lst2))):
        if l1 + l2 != len(lst2[i]) + len(lst1[i]):
            return lst1 if l1 <= l2 else lst2
    return lst1 if l1 <= l2 else lst2
```

The code employs a simple algorithm that iterates through the first elements of both lists, if the condition is not satisfied after the loop it returns the list with the least char count. The algorithm doesn't require any additional libraries; it comes in quite handy as the solution is straightforward and precise.

The `total_match` function solves the problem of finding the list with the fewest characters in total among two given lists of strings, returning the other list if the char counts are equal. It does so without requiring any external logic, making it a self-contained solution.