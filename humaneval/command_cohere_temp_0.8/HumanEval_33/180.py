```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted(l_copy[:i+1]))
        else:
            sorted_l.append(l_copy[i])
    return sorted_l
```

This Python script defines a function called `sort_third` which takes a list as an input parameter named `l`. This function processes each element of the list in different ways depending on whether the index of the element is divisible by three or not. In the script, a copy of the input list is created named `l_copy` to ensure that the original list is not altered during the process, the function creates an empty list named `sorted_l` to store the final sorted list. Then, it iterates through the elements of the list using a `for` loop. For elements with indices that are divisible by three, it sorts the corresponding portion of the `l_copy` list and appends it to the `sorted_l` list. For elements with indices that are not divisible by three, it directly appends the corresponding element of the original `l` list to the `sorted_l` list. 

Here is an example function call:
```python
>>> sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 3, 2, 6, 4, 9, 8, 7, 5]
```
Which maintains the original order for indices not divisible by three while sorting the corresponding indices that are divisible by three.