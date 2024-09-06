```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with several cases
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Test the function
print(get_positive(test_get_positive)) 

``` 
This code defines a function called **get_positive** that takes a list l as input and returns a new list containing only the positive elements from the original list.  It then uses list comprehension to filter out the positive numbers from the original list and then returns the new filtered list.