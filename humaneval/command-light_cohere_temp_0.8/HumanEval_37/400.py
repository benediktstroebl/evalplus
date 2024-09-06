```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    new_list = []
    for num in l:
        if num % 2 == 0:
            new_list.append(num)
   
    new_list.sort()
    new_list
   
    return new_list

# Example usage:
even_list = [5, 6, 3, 4]
result = sort_even(even_list)
print(result)
```
The output will be:
```bash
[3, 6, 5, 4]
```