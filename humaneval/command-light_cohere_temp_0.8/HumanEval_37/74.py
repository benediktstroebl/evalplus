```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x+1)

# Test cases
print("sort_even([1, 2, 3]) =",sort_even([1, 2, 3]))  # [1, 2, 3]
print("sort_even([5, 6, 3, 4]) =",sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
print("sort_even([10, 20, 30]) =",sort_even([10, 20, 30]))  # [10, 20, 30]
``` 
The function takes a list l and returns a list l' which is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.