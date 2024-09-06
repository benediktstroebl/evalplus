Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. 

To follow the problem statement, we should also include tests in the script. Feel free to add more tests to ensure the function behaves as expected. Here are two test cases to get you started:
```python
# Tests:
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
This will verify that the function behaves as described in the provided solution. Feel free to add more tests to cover a variety of scenarios, such as corner cases, nested lists, and so on. 
If you plan to reuse this function in other scripts, you may want to consider adding additional error handling, optimization, and integration with the broader Python ecosystem, such as using descriptive variable names, utilizing docstrings, or employing decorators for better function management. 

Let me know if you'd like to dive deeper into any of these advanced practices!