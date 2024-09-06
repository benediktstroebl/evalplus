```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the values at positions not divisible by three are in l' and the values at positions divisible by three are in l' and sorted."""
    new_list = []
    for num in lst:
        if num % 3 == 0:
            new_list.append(num)

    new_list.append(num)
   
    new_list.append(num)
   
    return new_list
```
This Python code defines a function `sort_third` that takes a list `lst` as an argument. The function creates a list `new_list` to hold the elements from `lst` that are neither divisible by three. It then appends the particular number to `new_list` twice since it is divisible by three. Finally, the function returns `new_list`.