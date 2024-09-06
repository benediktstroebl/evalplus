```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the corresponding values in l' are sorted such that they are not divisible by three.
    """
    `def`s: list
    """
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    return new_lst
``` 
This script defines a function called `sort_third` that takes a list `lst` as an argument and returns a new list `new_lst`. The function works by iterating through the original list `lst` and checking if each element is divisible by 3. If the number is not divisible by 3, it adds the element to the new list. If the number is divisible by 3, it does nothing and simply returns the original list. This ensures that all corresponding values in the original list are sorted in such a way that they will not be divisible by three.