```python
def max_element(lst):
    if not_element(lst) == None:
        return None
    return max(lst, key=lambda x: x)

def not_element(lst):
    return max(map(lambda x: x, lst)) if isinstance(lst, list) else lst

# Unit tests
test = []
test. max his = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test. = = [1, 2, 3, 5, 6, 7, 8, 9, 10]
test. = []
def test_max_element():
    for value in test_list:
        actual = max_element(value)
        expected = None if not_element(value) else max(map(not_element, value))
        assert actual == expected, f"Failed test: {value} != {expected}"

test_max_element()
 ``` 
This code defines the function max_element which returns the maximum element in the list, based on a custom key function (lambda x: x). It then defines the function not_element that checks if the input is a list and returns the maximum value in the list using the map function. Finally, it defines a unit test function test_max_element, which tests the correctness of the max_element and not_element functions by comparing their results against the expected maximum values.