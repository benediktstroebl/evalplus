```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l
    in the odd index, while its values at the even index are equal to the values of the even index of l,
    but sorted.

    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    l = l.split()
    merged = []
    for i in range(len(l)):
        if i % 2 == 0:
            merged.append(l[i])
        else:
            merged.append(l[i]) + 1
    merged.append(l[i])
    return merged
``` 
This Python script defines a function named sort_even that takes a list l as input and returns a new list l' such that the elements in odd indices are the same as the corresponding elements in l, but are sorted. The function then creates a new list by splitting l into two parts: odd elements and even elements. Then, it merges the list back into a new list, called merged, by checking if the current element is an even number. Finally, the function returns the list l' as the result.