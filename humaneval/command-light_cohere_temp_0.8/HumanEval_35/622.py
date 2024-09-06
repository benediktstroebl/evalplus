```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    return max(lst, key=lambda x: x)

def test_max_element():
    try:
        result = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        print(result)
    except TypeError:
        print("Error:", sys.path)
```