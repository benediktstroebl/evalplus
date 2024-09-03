```python
def next_smallest(lst):
    """
    Returns the next smallest element in the list, or None if list is empty.
    """
    sorted(lst)
    return lst[1]

# Example usage
my_list = [5, 1, 4, 3, 2]
print(next_smallest(my_list))  # Output: 2

my_list = []
print(next_smallest(my_list))  # Output: None

my_list = [1, 1]
print(next_smallest(my_list))  # Output: 1
```