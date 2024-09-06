```python
def sort_third(lst):
    """Sorts the list l such that values that are not divisible by three are at the beginning"""
    new_lst = []
    for x in lst:
        if x % 3 != 0:
            new_lst.append(x_third(x))
        else:
            new_lst.append(x_third(x))
    return new_lst

# Test case 1
print(sort_third([1, 2, 3]))  # Expected output: [1, 2, 3]

# Test case 2
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected output: [2, 6, 3, 4, 8, 9, 5]

# Test case 3
print(sort_third([10, 10,20,30,40,70,60,50,40,30,20,10]))  # Expected output: [10, 10, 20, 30, 40, 40, 50, 60, 70]
```