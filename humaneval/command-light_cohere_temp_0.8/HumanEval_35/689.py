```python
def max_element(lst):
    if not_elements(lst):  # Base case: empty list
        return None
    max_element = lst[0]  # Initialize with first element
    for num in lst[1:]: 
        if num > max_element:
            max_element = num
    return max_element

def not_elements(lst):
    return not any(isinstance(num, (int, float)) for num in lst)

# Example usage
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(my_list)
print("Maximum element:", result)
```