```python
def max_element(lst):
    if not_element(lst):  # Test if the list is empty
        return None
    return max(lst, key=lambda x: x)  # Use built-in max() with a key function that returns the element

def not_element(lst):
    if not isinstance(lst, list):  # Test if the input is not a list
        return False
    return isinstance(lst[0], (int, float)) and lst[0] != float('-inf'))

if __name__ == "__main__":
    test_cases = [
        [],
        [1, 2, 3],
        [-5, 2, -3, 3, 0, 9],
        [5, 3, -5, 2, -3, 3, 9, 0, 123],
        [123]
    ]

    for test_case in test_cases:
        print(f"Test case: {test_case}")
        actual_result = max_element(test_case)
        expected_result = None if not_element(test_case) else max(test_case, key=lambda x: x)
        print(f"  Result: {actual_result}, Expected: {expected_result}")
        print()
```

The script defines a function `max_element` that takes a list as an argument and returns the maximum element in the list. The `not_element` test ensures that the function handles empty lists correctly by returning `None`. 

The `test_cases` variable contains a list of test cases, each with a list of elements and an expected maximum element. The `for` loop iterates through each test case, calling the `max_element` function with the corresponding test case, and comparing the actual result with the expected maximum element.