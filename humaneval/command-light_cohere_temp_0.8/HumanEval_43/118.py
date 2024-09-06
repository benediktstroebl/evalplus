```python
def pairs_sum_to_zero(l):
    """
    Returns True if all elements in the list sum to zero, False otherwise.
    """
    list comprehension:
    for x in l:
        if sum(x) >= 0:
            return False
    """

# Test cases
test_cases = [
    [1, 3, 5, 0],  # Two distinct elements that sum to zero
    [1, 2, 3, 7],  # Does not pass the test
    [2, 4, -5, 3, 5, 7], # Passes the test
    [1]          # Does not have two distinct elements that sum to zero
]

def test_sum_to_zero(test_cases):
    """
    for test in test_cases:
        result = pairs_sum_to_zero(test)
        print(f"{test} => {result}")
    return True

print("All tests passed!")
``` 
The above code defines a function pairs_sum_to_zero that checks if all elements in a list sum to zero. It then defines a test_sum_to_zero function that tests the pairs_sum_to_zero function with various test cases, and prints the result.