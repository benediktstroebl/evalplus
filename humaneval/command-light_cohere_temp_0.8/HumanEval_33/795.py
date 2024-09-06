```python
def sort_third(lst):
    """Sorts the list l such that values that are not divisible by three are at the beginning, and the values divisible by three are at the end.
    
    :type lst: list
    >def sort_third(lst):
        lst[::3] = lst[1:]
        lst = lst[:] + lst[::3] + lst[1:]
        return lst

# Test the function
if __name__ == "__main__":
    test_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_lst = sort_third(test_lst)
    print(test_lst)
```

This Python code defines a function `sort_third` that sorts a list `lst` such that values not divisible by three are at the beginning, and values divisible by three are at the end of the list. 

The function uses the list slicing technique to accomplish this, which shifts all values that are divisible by three to the end of the list and then appends these values to the beginning of the list.

The `test_lst` variable is then used to test the function, and the output is printed to the console.