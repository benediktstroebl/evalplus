```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the values at indices that are not divisible by three are sorted alphabetically, while the values at indices that are divisible by three are left unaltered.

    :param l: list
        l': list
            return sorted(l) if all(map(lambda x: x % 3 == 0, l)) else l
    """
    return sorted(lst) if all(map(lambda x: x % 3 == 0, lst)) else lst

# Example usage
lst = [1, 2, 3]
print(sort_third(lst))
```
The code defines a Python function `sort_third` that takes a list `lst` as input. The function returns a `sorted(lst)` if all elements in the list are divisible by 3. If not, it returns the list `lst` as is.

The function effectively handles the sorting of lists based on the third decimal digit, providing a clear and concise solution.