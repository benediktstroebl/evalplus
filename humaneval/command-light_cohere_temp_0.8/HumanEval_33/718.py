```python
def sort_third(lst):
    # a list comprehension to filter out numbers divisible by three
    divisible = [x for x in lst if x % 3 == 0]
    # sort the list with the filtered values
    return sorted(lst[divisible])
# Example usage
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
```