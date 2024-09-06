```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    l_copy = list(l)
    for i in range(len(l)):
        if l[i] % 3 == 0:
            l_copy[i] = l[i]
    else:
        l_copy[i] = l_copy[i] + [l[i]]
        l_copy[i] = [l_copy[i][j] for j in range(0, i)]
    return l_copy

# Test case
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```