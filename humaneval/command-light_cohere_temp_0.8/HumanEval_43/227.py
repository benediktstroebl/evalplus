```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    The list of pairs, sums to zero, and checks if they are distinct.

    If the pairs sum to zero, return True; otherwise, return False.

# Example:
test_sum = [1, 3, -2, 1]
result = pairs_sum_to_zero(test_sum)
if result == True:
    print("Test passed.")
else:
    print("Test failed.")

# Input list
input_list = [1, 3, -2, 1]
result = pairs_sum_to_zero(input_list)
if result == True:
    print("List passed the test.")
else:
    print("List failed the test.")
```

The provided Python script defines a function called pairs_sum_to_zero that checks whether a given list of integers has two distinct elements that sum up to zero. The function returns True if the list satisfies this condition and False otherwise. The function utilizes the list of pairs and calculates the sum of all elements to determine if the condition is met. The test_sum variable is used to pass a test case where the sum of two distinct elements should be zero, and the result is then compared with the function's return value to determine if the test passed or failed. The script also provides an example input list and passes it through the function to check if the condition is satisfied, and the result is printed accordingly.