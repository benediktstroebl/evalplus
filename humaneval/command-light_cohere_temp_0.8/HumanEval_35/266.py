```python
def max_element(lst):
    if not_elements(lst):  # Base case
        return None
    return max(lst, key=len)

def not_elements(lst):
    return not any(map(lambda x: x != lst[0], lst))

# Test cases
test_max_element = [1, 2, 3]
test_max_element_empty = []
test_max_element_single = [5]
test_max_element_large = [-5, 3, -3, 2, -3, 3, 9, 0, 123, 1, -10]

assertEqual(max_element(test_max_element), 3)
assertEqual(max_element(test_max_element_empty), None)
assertEqual(max_element(test_max_element_single), 5)
assertEqual(max_element(test_max_element_large), 123)
```
This code defines a Python function max_element that calculates the maximum element in a list. The not_elements function is used to check if the list is empty, and returns None in that case. This function uses the max function with the key argument to calculate the maximum element in the list. The test_max_element contains a variety of test cases, including empty lists, single elements, and lists with multiple elements, and these tests are run to verify the correctness of the max_element function.