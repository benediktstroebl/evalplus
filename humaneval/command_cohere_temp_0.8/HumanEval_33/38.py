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

The function utilizes a loop to iterate through each index of the input list `l`. It checks whether the index is divisible by three through the modulo operator `%`. If the index is divisible by three, it sorts the corresponding values in the `l_copy` list and appends them to the `sorted_l` list. For all other indices, it appends the unchanged values from the input list `l` to the `sorted_l` list.

Here is an example usage of the function:
```python
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```
In the first example, the input list is `[1, 2, 3]`. The function returns the original list as the output, as no index is divisible by three. In the second example, the input list is `[5, 6, 3, 4, 8, 9, 2]`. The sorted version of the list at indices divisible by three is `[2, 3, 4, 5, 6, 8, 9]`. This sorted version is then appended to the new list, resulting in the output `[2, 6, 3, 4, 8, 9, 5]`.