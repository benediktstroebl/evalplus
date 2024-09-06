```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    Args:
        l (list)
    Returns:
        l' (list)
    """
    l_copy = l.copy()
    done=True
    l_copy[:]
    done_indic = False
    for i in range(len(l)):
        if l[i]%3 == 0 and not done_indic:
            l_copy[i] = l[i]
        done_indic = True
    for j in range(i,len(l)):
        if l[j]%3 == 0 and l[i]!=l[j]:
            l_copy[j] = l[i]
    return l_copy

# Test the function
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
 ```