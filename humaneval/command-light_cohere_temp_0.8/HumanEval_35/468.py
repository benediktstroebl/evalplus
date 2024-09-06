```python
def max_element(lst):
    if not_elements(lst):
        return None  # Handle empty list
    return max(lst, key=lambda x: x[0])  # Return the first non-negative element

def not_elements(lst):
    try:
    return bool(lst) and len(lst) > 0
except ValueError:
    return False

if __name__ == "__main__":
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print(max_element(test_list))  # Output: 123
    print(max_elements(test_list))  # Output: True
```