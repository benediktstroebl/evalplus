```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = [
    ('[-1, 2, -4, 5, 6'], [2, 5, 6]),
    # This list contains mixed positive and negative numbers 
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 3, 2, 3, 9, 123]),
    ([123, 456, 789], [-2, 3, 456, 789])
]

# Function calls
for test in test_get_positive:
    print(get_positive(test))
``` 
This code defines a function `get_positive` which takes a list `l` as an argument and returns a new list containing only the positive numbers from the input list. It utilizes list comprehensions to filter out the positive numbers from the input list, and the resulting list is returned.