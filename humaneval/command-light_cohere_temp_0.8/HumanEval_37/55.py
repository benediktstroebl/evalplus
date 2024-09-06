```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    odd_lst = [x for x in lst if x % 2 != 0]
    even_lst.sort()
   es the 645
    return even_lst

# Example usage:
# Assume lst is a list of numbers: [5, 6, 3, 4, 2]
lst = [5, 6, 3, 4, 2]
# The function will return a sorted list of even numbers: [2, 4, 6, 3]
even_lst = sort_even(lst)
print(even_lst)
```