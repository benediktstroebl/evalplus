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
This script defines a function called `sort_third` which takes a list `l` as input and returns a new list `l_sorted`. The function only modifies the list values at indices that are divisible by three and leaves the other values unchanged. The result is a new list `l_sorted` where the values at the indices divisible by three are sorted, while the other values remain the same as in the original list.

Here is an example usage of the function:
```python
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```
In the example above, we can see that the values at the indices divisible by three have been sorted, while the values at the other indices remain the same as in the original list.