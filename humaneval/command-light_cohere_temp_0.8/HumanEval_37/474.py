```python
def sort_even(lst):
    """This function sorts an input list l such that all the odd index values are kept in the same relative order, while even index values are sorted in ascending order.
    """ return sorted(lst, key=lambda x: not_even(x))
 
def not_even(x):
    """This function checks if the index of x is even or not."""
    return x % 2 == 0
 
#Example usage
even_list = [5, 6, 3, 4]
sorted_even = sort_even(even_list)
print("Even list sorted:", sorted_even)

#Test case 1
odd_list = [1, 2, 3]
sorted_odd = sort_even(odd_list)
print("Odd list sorted:", sorted_odd)
```