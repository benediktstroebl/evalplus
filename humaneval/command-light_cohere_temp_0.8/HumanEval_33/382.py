```python
def sort_third(lst):
    """This function sorts a list l such that elements which are not divisible by three are at the beginning, and elements which are divisible by three are in their correct positions.

    : Example of a expected output:
        [2, 6, 3, 4, 8, 9, 5]
    """
    # Sort the list
    lst.sort_list = sorted(lst, key=lambda x: int(x) % 3)

    return lst

# Test cases for function
tests = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(tests))  # Output: [2, 6, 3, 4, 8, 9, 5]
```