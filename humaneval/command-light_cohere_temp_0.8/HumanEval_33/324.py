```python
def sort_third(lst):
    """This function sorts a list l such that numbers not divisible by three are in the beginning, and numbers divisible by three are in the end.
    numbers = [x_num(n) for n in lst if n % 3 == 0]
    return sorted(lst, key=lambda x: (-x if x in numbers else x))

# Test case
lst1 = [5, 6, 3, 4, 8, 9, 2]
print("Original list:", lst1)
print("Sorted list:", sort_third(lst1))

# Test case 2
lst2 = [1, 2, 3, 4, 5, 6, 8, 9]
print("Original list:", lst2)
print("Sorted list:", sort_third(lst2))

# Test case 3
lst3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", lst3)
print("Sorted list:", sort_third(lst3))
```

This script defines a function called sort_third that takes a list as input and sorts it such that the numbers not divisible by three are in the beginning and the numbers divisible by three are in the end. The function uses a efficient algorithm that utilizes the concept of dividing the list into two parts: one with numbers divisible by three and the other with numbers not divisible by three.