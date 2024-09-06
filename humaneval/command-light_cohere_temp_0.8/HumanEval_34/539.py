```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    set1 = set(l)
    return list(set1)

# Test the function with sample input
test_case = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test Case 1:", unique(test_case))

# Test the function with another list
test_case_2 = [1, 2, 3, 4, 5, 6, 7]
print("Test Case 2:", unique(test_case_2))
``` 
This code defines a function unique that takes a list l as an argument and returns a new list containing unique elements from the original list. It uses the
 set1 data structure to remove duplicates and return the unique elements in sorted order.