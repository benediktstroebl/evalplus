```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    odd_lst = [x for x in lst if x % 2 != 0]
    return even_lst

# Example usage:
even_lst = sort_even([1, 2, 3, 4, 5, 6])
print(even_lst)  # Output: [2, 3, 4, 5, 6]
```