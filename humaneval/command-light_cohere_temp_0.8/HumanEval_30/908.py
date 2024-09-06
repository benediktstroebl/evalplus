```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with different lists
lists = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    []
]

for test_list in lists:
    print(get_positive(test_list))
``` 
This script defines a function get_positive that takes a list as an argument and returns a new list with only the positive elements from the original list.  The function uses list comprehension to filter out the positive elements from the input list.