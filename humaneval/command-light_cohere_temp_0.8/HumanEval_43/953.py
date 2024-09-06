```python
def pairs_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst)

# Test function to check if the function correctly identifies pairs adding up to zero
def test_pairs_sum_to_zero(test_list):
    return test_pairs_sum_to_zero(test_list)

# Test list containing lists of numbers where some pairs add up to zero
test_list = [[1, 3, 5, 0], [1, 2, 3, 7], [-2, 1, 5, 3], [1]]

# Call the test function with the test list
result = test_pairs_sum_to_zero(test_list)

# Print the result
if result:
    print("Passed test!")
else:
    print("Failed test.")
``` 
This code defines a function `pairs_sum_to_zero` that determines whether every element in a list pairs adds up to zero. It also contains a test function `test_pairs_sum_to_zero` which verifies the function's correctness by passing the test list. The code then sets up a test list, calls the test function with it, and finally prints out a pass/fail message based on the result.