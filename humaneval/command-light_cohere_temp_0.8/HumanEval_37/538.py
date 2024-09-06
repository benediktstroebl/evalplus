```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.

    :param list l: The list of numbers
    :return: A list of numbers sorted in even index
    """
    l_even = []
    for num in l:
        if num % 2 == 0:
            l_even.append(num)
    l_even.append(num)
    l = l_even
    return l
```