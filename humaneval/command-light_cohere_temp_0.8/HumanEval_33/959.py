```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    """
    lst[:] = sorted(lst[:], key=lambda x:int(x) % 3)
    return lst
```
This function, sort_third, takes a list l as input and returns a new list lst that ensures elements divisible by three are in the same order as in l. The function uses the language to sort the list in a way that preserves the relative order of the elements that are divisible by three, and puts the other elements in the original order. 

This is achieved by using the built-in Python function `sorted`, and a lambda function that returns the remainder when dividing the element by 3.