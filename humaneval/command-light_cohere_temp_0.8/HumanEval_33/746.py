```python
def sort_third(lst):
    """Sorts the list l such that all elements which are divisible by three are moved to the front, and the rest are moved to the back.

    # Sort the key list l, moving all divisible numbers to the front, and the rest to the back.
    lst.sort_keys() = 'range(0, len(lst))
    # 0 -> [0] (first element) and then numbers greater than 3
    lst[::] = lst[i] for i in range(3, len(lst))
    lst[i] = lst[::] for i in range(1, len(lst)-3)
    # Now lst is sorted in a way that numbers > 3 are first, and numbers divisible by 3 are in the back.
    return lst

```
Now you can use this function to sort any list in the desired way.