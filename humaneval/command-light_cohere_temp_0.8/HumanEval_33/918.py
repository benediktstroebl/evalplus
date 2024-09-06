```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    new_list = []
    for num in l:
        if (num % 3) == 0:
            new_list.append(num)
        else:
            new_list.append(num)
        new_list.append(num)
    new_list.append(num)
    new_list.sort()
   ss ()
    new_list
    return new_list

# Example of of passing the test:
print(sort_third([1, 2, 3, 4, 5, 6, 7, 8]))
 ```