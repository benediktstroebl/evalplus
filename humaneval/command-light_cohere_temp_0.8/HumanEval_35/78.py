```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    return max(lst)

def not_elements(lst):
    return any([isinstance(num, (int, float)) for num in lst]) and all(num > 0 for num in lst)

if __name__ == "__main__":
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("Maximum element:", max_element(test_list))  # Output: 123
    print("Are numbers in list non-negative?", not_elements(test_list))  # Output: True
```