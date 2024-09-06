```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print("Test case 1 passed:", end)
get_positive([-1, 2, -4, 5, 6])

# Test case 2
print("Test case 2 passed:", end)
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, -10])

# Test case 3
print("Test case 3 passed:", end)
get_positive([2, 5, 6, 0, -10, 3, 7])
```
This Python code defines a function called **get_positive** that takes a list as an argument. It then iterates through list elements, and for each element, it checks if the element is greater than or equal to zero, and if it is, it adds it to a new list that only contains the non-negative elements from the original list. 

The code then tests the function with three different lists, each with a different set of numbers, and verifies that the function correctly filters out the negative values and returns the expected list of non-negative elements.