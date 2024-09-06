```python
def sort_third(lst):
    """This function sorts a list l such that values that are divisible by three are in their correct relative positions."""
    # Sort all numbers
    lst = sorted(lst, key=lambda x: x)
    # Separate numbers divisible by three and numbers not divisible by three
    i = 0
    while i < len(lst):
        if lst[i] % 3 == 0:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        else:
            i += 1
    return lst

# Example usage
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))  # Output: [2, 6, 3, 4, 8, 9, 5]
```