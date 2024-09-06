Here's a Python script that contains a function named `double_the_difference` which solves the problem as per the given instructions:
```python
def double_the_difference(lst):
    odd_and_valid = [num for num in lst if num % 2 == 1 and num >= 0 and isinstance(num, int)]
    return sum(num ** 2 for num in odd_and_valid)
```

This function first filters valid odd numbers from the input list using a list comprehension. It checks for three conditions: oddness (`num % 2 == 1`), non-negative (`num >= 0`), and integrity of the number (`isinstance(num, int)`). The squares of these valid odd numbers are then summed, resulting in the answer to the problem. This approach ensures that only valid odd integers are considered while ignoring any invalid entries. 

The function returns 0 if the input list is empty, adhering to the specified empty input case. 

To ensure the function behaves as expected, it's essential to incorporate tests that cover multiple scenarios. These tests can check the function's behavior against edge cases, like empty lists, invalid entries, and different combinations of valid and invalid odd numbers. Here are some example tests to get you started:
```python
# Test the basic functionality
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([-1, -2, 0]) == 0  

# Test with an empty list
def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0  

# Test with some negative numbers
def test_double_the_difference_with_negatives():
    assert double_the_difference([1, -3, 5, -2]) == 4  
```

These sample tests cover various scenarios, including empty lists and lists containing both positive and negative odd numbers. You can add more tests depending on edge cases and specific requirements. 
Remember, when defining test functions, it's best to use the `pytest` framework and define test functions starting with `test_`. This naming convention allows `pytest` to automatically discover and run the tests.