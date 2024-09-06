```python
def max_element(lst):
    if not_number(lst) == None:
        return None
    elif len(lst) == 0:
        return 0
 
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element
 
def not_number(lst):
    for item in lst:
        if isinstance(item, (int, float)):
            return True
    return False
 
# Test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([1, 2, 3, ,4, 5, 6, 7]))  # Output: 5
print(max_element([18, 22, 15, 12, 9, 13, 10]))  # Output: 22
```