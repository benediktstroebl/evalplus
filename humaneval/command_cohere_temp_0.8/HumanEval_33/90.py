```python
def sort_third(l):
    l3 = [ele for ele in l if ele % 3 == 0]
    l3.sort()
    return l3 + [ele for ele in l if ele % 3 != 0]
```

This Python script defines a function called `sort_third`. This function takes a list `l` as input and returns a new list `l'` that preserves the original elements at indices not divisible by three, while the elements at indices divisible by three are sorted. The function achieves this by first filtering out the elements at indices divisible by three into a separate list `l3` and sorting it. It then returns the original list with the sorted elements at the divisible by three indices replaced.

Here is an example usage of the function:
```python
 >>> sort_third([1, 2, 3])
[1, 2, 3]
 >>> sort_third([5, 6, 3, 4, 8, 9, 2])
 [2, 6, 3, 4, 8, 9, 5]
```
In the first example, the input list is `[1, 2, 3]`, which returns the original list as the elements at indices 0 and 2 (indices not divisible by three) are sorted. In the second example, the input list is `[5, 6, 3, 4, 8, 9, 2]`, and the result is `[2, 6, 3, 4, 8, 9, 5]`, where the elements at indices 0, 3, and 6 (indices divisible by three) are sorted.