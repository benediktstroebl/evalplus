```python
def sort_even(lst):
    """This function sorts a list l according to the even items' values,
    keeping the relative order of the odd items.
    Input: lst = [1, 2, 3, 5, 6]
    return sorted(lst, key=lambda x: x % 2)

# Test the function with various inputs
if __name__ == "__main__":
    lst1 = [1, 2, 3]
    lst2 = [5, 6, 3, 4]
    lst3 = [0, 1, 2, 3]

    print("First list:", lst1)
    print("Sorting:", sort_even(lst1))
    print("Second list:", lst2)
    print("Sorting:", sort_even(lst2))

    print("Third list:", lst3)
    print("Sorting:", sort_even(lst3))
```

This script defines a function `sort_even` that sorts a list based on the values of the even items. It then passes these tests the A list of lists [1, 2, 3] and [5, 6, 3, 4] to illustrate how the function works. The script also includes a test case with a list of numbers [0, 1, 2, 3] to demonstrate the function's behavior with different types of data.