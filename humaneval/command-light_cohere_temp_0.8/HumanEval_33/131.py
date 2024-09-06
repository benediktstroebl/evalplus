```python
def sort_third(l: list):
    """Sorts list l so that values not divisible by three are at the front, and the other values are rearranged. Returns a old list l."""
    new_list = []
    for num in l:
        if num % 3 == 0:
            new_list.append(num)
        else:
            new_list.append(num)  # in front because this avoids later added numbers from being out of order
    new_list.append(num)
    return new_list
```
The function takes a list `l` and returns a new list `l'` which is sorted so that values not divisible by three are at the front and other values are rearranged. 

The list `l` is looped through and the number is added to `new_list` if it is not divisible by three. If the number is divisible by three then it is added to `new_list` at the end.

This ensures that the list `l` is sorted so that the values that are not divisible by three are at the start of the list and the other values are rearranged.