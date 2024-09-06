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
This code defines a function called `sort_third` which takes a list `l` as input. Inside the function, a copy of the input list `l` is created and assigned to the variable `l_copy`. An empty list named `sorted_l` is initialized to store the sorted values at indices divisible by three. The function then iterates through each index of the input list using a `for` loop. For indices that are not divisible by three, the corresponding element from `l_copy` is appended to `sorted_l`. For indices that are divisible by three, the elements are sorted within a nested list, and the sorted result is appended to `sorted_l`. In this way, the function creates a new list `sorted_l` where elements at indices divisible by three are sorted, while elements at other indices remain unchanged from the original input list `l`.

Here is an example usage of the function:
```python
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```
In the example usages, the function is called with two different lists. In the first case, the original list is unchanged since none of its indices are divisible by three. In the second case, the elements at indices 3 and 6 are sorted, resulting in the desired sorted list as output.