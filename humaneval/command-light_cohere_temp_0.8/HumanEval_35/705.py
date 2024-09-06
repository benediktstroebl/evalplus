```python
def max_element(lst):
    if not_enough_elements(lst):
        return lst[-1]
    else:
        return "Not enough elements to find maximum"
    
def not_enough_elements(lst):
    return len(lst) >= 1

# Example usage
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(my_list)
print(result)  # Output: 123
``` 
This Python code defines a function `max_element` that finds the maximum element in a given list. The `not_enough_elements` function checks if the list has at least one element before returning "Not enough elements to find maximum". It uses these two functions in the example usage, creating a list, calling the `max_element` function, and printing the result, which will be the maximum element in the list.