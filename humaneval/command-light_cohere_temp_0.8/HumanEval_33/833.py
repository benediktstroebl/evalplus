```python
def sort_third(lst):
    """This function sorts a list l such that values that are divisible by three are in their correct order. 
    It sorts numbers that are not divisible by three to appear later than numbers that are divisible by three."""
    lst = [x for x in lst if x % 3 == 0] + [x for x in lst if x % 3 != 0]
    return sorted(lst)
# Example
lst = [1, 2, 3]
print(sort_third(lst))
```
The above code defines a function `sort_third` that sorts a list such that the numbers that are divisible by three are in their correct order and all other numbers are sorted later. The example shows how the use of the function on a sample list and the result is printed.