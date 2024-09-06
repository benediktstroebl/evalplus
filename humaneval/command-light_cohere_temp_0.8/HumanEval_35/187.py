NAVBAR

def max_element(lst):
    """Return maximum element in the list"""
    if not lst:
        return 0  # Return 0 if the list is empty
    if len(lst) == 1:
        return lst[0]
    max_element = max(lst)
    return max_element

# Test the function with various test cases
test_max_element = max_element  # Binding the function into a test case

should_test_cases = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Loop through test cases and assert the result is as expected
for case in should_test_cases:
    assert max_element(case) == case[1]

Now, feel free to use this function with your own lists and enjoy the simplicity and readability!