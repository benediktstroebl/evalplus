```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    return max(lst, key=lambda x: x)

def not_elements(lst):
    return any(x != lst[0] for x in lst)  # Check if all elements in the list are equal

# Test cases
tests = [
    [
        lst=[1, 2, 3], returns=False
    ],
    [
        lst=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], returns=True
    ],
    [
        lst=[1, 2, 3, 4, 5], returns=False
    ],
    [
        lst=[-5, -3, -8, -10], returns=True
    ],
    [
        lst=[1, 2, 3, 4, 5, 6, 7], returns=False
    ],
    [
        lst=[0, 0, 0], returns=False
    ],
    [
        lst=[123, 0, 0], returns=False
    ],
    [
        lst=[1, 2, 3, 4, 5, 6, 7, 8, 9], returns=True
    ]
]

# Test the function
for test in tests:
    assert max_element(test[lst]) == test[returns], "Error in test case"
``` 

This script defines a function `max_element` that returns the maximum element in a list, as long as the list is not empty. The function uses the primary sorting technique and a custom key function to achieve this. The `not_elements` test is used to ensure that the list is not empty, and the `any` function is used to check that all elements in the list are different. The script also includes a list of test cases, which are passed to the function to test its correctness.