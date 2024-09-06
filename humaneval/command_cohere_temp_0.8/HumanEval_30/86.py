Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a new list containing only positive numbers from the input list `l`. 
The function is called with two test cases in the script to ensure that it follows the behavior defined in the problem:
```python
test_cases = [[(-1, 2, -4, 5, 6), [2, 5, 6]], 
             [(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10), [5, 3, 2, 3, 9, 123, 1]]]
for case in test_cases:
    nums, expected = case
    actual = get_positive(nums)
    assert actual == expected, f"Expected {expected}, but got {actual} for input {nums}"
``` 
The tests succeed for the two provided examples, and the function adheres to the problem's specified functionality. You can use this script as a standalone solution to the issue. If you have any more concerns or require assistance with anything else, please include them so that we can address them and offer practical insights. Do not hesitate to ask if you have any further questions or if you would like to explore other topics.