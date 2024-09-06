```python
def sort_third(lst):
    """Sorts a list l such that all numbers not divisible by three are at the beginning, and all numbers divisible by three are at the end.
    # Sort the particular list using the numbers that are divisible by three, and for the corresponding numbers that are not divisible by three, sort them as they are in the original list.
    # Initialize two list of numbers that are divisible by three.
    v = [all numbers divisible by three
    lst = [v] + l
    # Sort all remaining numbers
    for i in lst:
        if i != v:
            lst.insert(0, i)
    # Sort all numbers that are not divisible by three
    l.sort(l)
    return lst
```