Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

To test this function, you can run the following code:
```python
TestIncList = dict(
    good_cases = [
        ([], []),
        ([1], [2]),
        ([1, 2, 3], [2, 3, 4]),
        ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124])
    ]
)

print(tests.test_function_dict(incr_list, TestIncList))
```
The above code uses the `tests` module to test the `incr_list` function with the test cases provided in the `TestIncList` dictionary. The result of running this code should be `True` since all test cases in `TestIncList` should now pass with the updated `incr_list` function.