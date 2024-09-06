```python
def max_element(lst):
    if not_elements(lst):
        return 0  # Return 0 for empty list
    max_element = lst[0]
    for num in lst[1:]:
        if num > max_element:
            max_element = num
    return max_element

def test_max_element(test_list):
    for lst in test_list:
        got_max = max_element(lst)
        print("Got:", got_max)
        expect = [123]
        assert got_max == expect, f"Expectation not met: {expect}, {got_max}"

```
In this script, we have defined the `max_element` function that takes a list `lst` as input and returns the maximum element in that list. The `test_max_element` function provides a simple test suite with the `test_list` and checks the `max_element` function's correctness against the provided test cases.