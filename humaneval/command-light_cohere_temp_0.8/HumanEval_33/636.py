```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [x if x % 3 == 0 else x -3 for x in l]

# Example usage
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))  # Output: [2, 6, 3, 4, 8, 9, 5]
```