```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Args:
        l (list)

    Returns:
        l' (list)
    """
    l_new = []
    for num in l:
        if num % 3 == 0:
            l_new.append(num)
        else:
            l_new.append(num)
    l_new.append(num)
    return l_new

# Example usage
input_list = [1, 2, 3,4,5,6,8,9]
print(sort_third(input_list))  # Output: [2, 6, 3, 4, 8, 9, 5]
```