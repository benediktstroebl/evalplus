```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted. """"""
    this function uses the principle of moving numbers that are divisible by three to the front and the numbers that are not divisible to the back.
    """The following is are the test cases to pass:
    1. [1, 2, 3] -> [1, 2, 3]
    2. [5, 6, 3, 4, 8, 9, 2] -> [2, 6, 3, 4, 8, 9, 5]
    3. [5, 6, 3, 4, 8, 9, 2, 7] -> [2, 6, 3, 4, 8, 9, 5, 7]
    4. [10, 11, 12] -> indefinite, not applicable
    """
    return sorted(lst, key=lambda x:int(x) % 3 == 0)
```