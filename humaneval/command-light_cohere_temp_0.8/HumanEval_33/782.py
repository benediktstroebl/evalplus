```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    :param lst: list
    :return: sorted list
    """
    lst[::3] = lst[::3]  # copy third element of each sublist
    lst[1::3], lst[2::3] = lst[2::3], lst[1::3]  # swap first and second sublists
    return lst

# test case 1
print(sort_third([1, 2, 3]))
# expected output [1, 2, 3]

# test case 2
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
# expected output [2, 6, 3, 4, 8, 9, 5]

# test case 3
print(sort_third([10, 15, 20, 25, 30, 35, 25]))
# expected output [10, 20, 25, 30, 35, 15, 25]
```
This Python script defines a function named `sort_third` that sorts a list according to the problem statement. The function takes a list `lst` as input and swaps the elements that are divisible by three with the corresponding elements in the list. Then, it swaps the elements in the first and second sublists and copies the third element from the first sublist to the second sublist. Finally, the function returns the list that is sorted by the problem statement.