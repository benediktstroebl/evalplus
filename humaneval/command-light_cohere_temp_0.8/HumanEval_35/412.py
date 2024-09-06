```python
def max_element(lst):
    if not_list(lst):  # Check if list is valid
        return "Input should be a list"
    if not len(lst) or lst == []:  # Handle empty list
        return "List is empty"
    max_val = max(lst)  # Find the maximum element
    return max_val

# Unit tests
test_max_element = [
    dict(
        zip(
            [
                "Input: [-5, 3, 9]",
                "Expected max element: 9",
                "Got: -5"
            ],
            [max_element])
        )
    )
]
```  This code defines a function max_element that takes a list lst as input and returns the maximum element in the list. The function also has unit tests.