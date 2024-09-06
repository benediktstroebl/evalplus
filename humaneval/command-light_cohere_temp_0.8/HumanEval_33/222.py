```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
   >>>
    list(map(lambda x: (x <= 3) and x % 3 != 0) for x in l))
    return l

# Test the function
test_list = [5, 6, 3, 4, 8, 9, 2]
test_list2 = [1, 2, 3, 4, 5, 6, 7]
print(sort_third(test_list)) == [2, 6, 3, 4, 8, 9, 5])
print(sort_third(test_list2)) == [1, 2, 4, 5, 6, 7]
```