```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal to the values of the even indic of l, but sorted.
    return:
    l[:] = sorted(l, key=lambda x: not(x) and x[1] % 2 == 0)
    l = l[:]
    return l

# test the function
test_list = [5, 6, 3, 4]
print(sort_even(test_list))  # [3, 6, 5, 4]
 ```