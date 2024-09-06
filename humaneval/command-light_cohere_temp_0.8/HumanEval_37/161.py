```python
def sort_even(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    else:
        even_lst.append(num + 1)
    return even_lst
```