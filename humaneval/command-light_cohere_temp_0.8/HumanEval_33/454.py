```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the 
    indicies that are not divisible by three, while its values at the indic that are divisible by three 
    are equal to the values of the corresponding indic of l, but sorted.

    Args:
        l (list)

    Returns:
        l' (list)
    """
    lst[::3] = lst[::3] + [lst[i] for i in range(len(lst)) if i % 3 == 0]
    return lst

# Example usage
input_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(input_list))
```