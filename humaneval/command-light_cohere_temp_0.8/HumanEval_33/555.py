```python
def sort_third(lst):
    """This function sorts a list so that values divisible by three appear last.

    : We elements [list l and return a new list l' such that all values divisible by three are at the end.
    """
    list comprehension:
        lst[:::3] = [x for x in lst if x % 3 == 0]
    lst = lst[:-::3] + lst[::3:]
    """
    return lst

# Test cases:
print(sort_third([1, 2, 3]))    # Expected output: [2, 3, 1]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # Expected output: [2, 6, 3, 4, 8, 9, 5]
```
This Python script defines a function called `sort_third` that takes a list as input and returns a new list where values divisible by three are at the end, with the original list's other values. The script then provides two test cases that demonstrate the function's expected behavior.