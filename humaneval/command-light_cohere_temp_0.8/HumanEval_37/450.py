```python
def sort_even(lst):
    even_set = set(lst[1::values])
    lst[:] = [e for e in lst[0] if e in even_set]
    lst.append(e)
    sorted(lst)
    return lst

# Example usage
input_list = [5, 6, 3, 4, 2]
result_list = sort_even(input_list)
print(result_list)
```