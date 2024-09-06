```python
def sort_even(lst):
    even_list = [el for el in lst if el % 2 == 0]
    return even_list

even_list = sort_even([1, 2, 3])
print(even_list)
```