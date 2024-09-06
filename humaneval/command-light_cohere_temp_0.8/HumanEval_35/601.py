```python
def max_element(lst):
    if not_num_el(lst):
        return float('-inf')
    else:
        return max(lst)

def not_num_el(lst):
    try:
        for num in lst:
            if type(num) != float:
                return False
        return True

# Example usage
lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(lst))  # Output: 123
print(max_element([5, 3, -5]))   # Output: 5
print(max_element([1, 2, 3, -100])) # Output: float('-inf')
```
The script defines a function `max_element` that takes a list `lst` as input and returns the maximum element in the list. It utilizes a fact-checking for different types of elements using the `not_num_el` helper function, which returns `True` if all elements in the list are of type `float`, indicating that they are numbers.  The maximum element is then returned by the `max` function.