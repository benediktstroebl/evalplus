```python
def max_element(lst):
    if not_elements(lst):  # Base case: empty list
        return None
    
    max_val = max(lst)
    max_index = lst.index(max_val)
    return lst[max_index]

def test_max_element():
    test_lists = [
        [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
        [1, 2, 3, -20],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, -100],
        [5, -6, -8]
    ]
    
    expected = [3, -20, -100, -8]
    for test_list in test_lists:
        actual = max_element(test_list)
        assert actual == expected, f"Error in test list: {test_list}"

if __name__ == "__main__":
    test_max_element()
```
This script defines the function `max_element` that finds the maximum element in a list, considering empty lists as valid inputs. The `test_max_element` function contains multiple test lists and asserts that the output of `max_element` function matches the expected result for each test. 

Finally, the `if __name__ == "__main__":` block ensures that the code is executed only when the script is run directly, not imported.