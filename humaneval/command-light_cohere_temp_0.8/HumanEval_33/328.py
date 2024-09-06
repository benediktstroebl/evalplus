```python
def sort_third(lst):
    """This function sorts a list l such that values not divisible by three are at the beginning, and the values divisible by three are sorted correspondingly.

    Args:
        lst (list) : the list of integers

    Returns:
        new_lst (list) : the list where values divisible by three are at the beginning, and the rest is sorted
    """
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    new_lst.append(num)
   
    new_lst.sort()
   new_lst.append(num)
   
    new_lst
    return new_lst
``` 
This script defines a function `sort_third` that takes a list `lst` as an argument. The function creates a list `new_lst` and initializes it as an empty list. Then, it iterates through the list and checks if the number is divisible by three. If the condition is true, it appends this number to the beginning of the `new_lst` list. Then, it appends the number to the end of the `new_lst` list and sorts the `new_lst` using the `sort` method. Finally, it returns the list `new_lst` which contains the numbers from the original list, but with values divisible by three at the beginning and the rest of the values sorted.