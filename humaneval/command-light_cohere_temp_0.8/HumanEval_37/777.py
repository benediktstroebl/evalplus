```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    """
    list l, sort()
    l.extend(lambda x: x%2 == 0)
    l.select_even()
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i], l[len(l) + i] = l[len(l) + i], l[i]
    return l

# Test the function
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
print(result)
```