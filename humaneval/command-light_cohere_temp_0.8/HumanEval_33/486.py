```python
def sort_third(lst):
    """This function sorts a list so that elements that are divisible by three appear later.
    @type lst: list
    @return: list
    """
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
    else:
            new_lst.append(num) ounes the
    return new_lst
```