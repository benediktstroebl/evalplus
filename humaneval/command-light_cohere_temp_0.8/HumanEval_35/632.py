```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list is empty!")
    return max(lst)

def test_max_element():
    try:
        _test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        max_element(_test_list)
        print("Passed test!")
    except ValueError as e:
        print(f"Test failed: {e}")

# Run tests and display results
test_max_element()
```