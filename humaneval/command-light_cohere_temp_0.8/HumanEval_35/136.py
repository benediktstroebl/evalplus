```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list is empty.")
    if len(lst) == 1:
        return lst[0]
    max_num = max(lst)
    return max_num

def not_elements(lst):
    return not any(map(lambda x: x <= 0, lst))

# Example usage
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(test_data))  # Output: 123
print(max_elements(test_data))  # Output: True
```