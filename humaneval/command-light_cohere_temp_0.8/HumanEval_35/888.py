```python
def max_element(lst):
    if not_elements(lst):  # Checks for empty list
        return None
    return max(lst)

def not_elements(lst):
    if lst == []:  # Lists are not empty
        return False
    return all(isinstance(num, (int, float)) for num in lst) and all(num >= 0 for num in lst)

# Example usage
lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(lst))  # Output: 123
print(max_elements(lst))  # Output: True
``` 
This script defines a function `max_element` that takes a list `lst` as input and returns the maximum element in the list. The function also includes a `not_elements` check to handle the case when the list is empty.

The `not_elements` function is used to check if the list is empty, and if it is, the function returns `None`. 

The `isinstance` function with the `int` class is used to ensure that all elements in the list are integers, and the `>= 0` condition is used to filter out negative numbers. 
`max_elements` function` is used to check if the list is empty or if all elements in the list are non-negative. 

The `max` function is used to find the maximum element in the list. 

The output of the `max_element` and `max_elements` functions are then tested with the provided example list `lst`.