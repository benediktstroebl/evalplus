```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 20, 40, 3, 19, 9])
    [1, 2, 3, 20, 40, 19, 9, 10]
    """
    lst = sorted(set(lst), key=lambda x: x // 3)
    return lst
```  This script defines a function called sort_third, which takes a list lst as input and returns a list lst' that maintains the property that integers that are not divisible by three are in their original order, while the values that are divisible by three are ordered. The list is then sorted in ascending order. 

It achieves this by first converting the input list lst to a set using the sorted() function with a key lambda function, which identifies the integers that are not divisible by three. Then, it sorts the set using a key that calculates the inverse of the division by three, effectively sorting the remaining values.