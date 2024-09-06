```python
def sort_even(lst):
    even_lst = []
    odd = 0
    while len(lst) > 0:
        if lst[len(lst) // 2] == even:
            even_lst.append(lst[even])
        even = 1
        else:
            even_lst.append(lst[odd])
            odd = 1
            lst.remove(lst[len(lst) // 2), lst)
    return even_lst
# Example usage
even_list = sort_even([1, 2, 3])
print("Sorted even integers:", even_list)
```