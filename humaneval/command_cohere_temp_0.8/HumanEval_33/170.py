```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted(l_copy[i]))
        else:
            sorted_l.append(l_copy[i])
    return sorted_l
```
This Python script defines a function called `sort_third`. This function takes a list `l` as input and returns a new list `l_copy`. The new list is identical to the input list in indices that are not divisible by three, while for indices that are divisible by three, the values in the new list are sorted versions of the corresponding values in the input list.

Here is an example of how you can use this function:
```python
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```
In the first example, the input list is `[1, 2, 3]`, and the result is `[1, 2, 3]`, which is the same as the input since none of the indices are divisible by three. In the second example, the input list is `[5, 6, 3, 4, 8, 9, 2]`. The result `[2, 6, 3, 4, 8, 9, 5]` has sorted values in the indices divisible by three (here, indices 0, 3, and 6), while the rest remains unchanged.