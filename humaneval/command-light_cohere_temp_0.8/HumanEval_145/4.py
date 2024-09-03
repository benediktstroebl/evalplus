```python
def order_by_points(nums):
    # Initialize a list to store the sorted integers
    sorted_nums = []
    
    # Add each integer to the list and sort it
    for num in nums:
        sorted_nums.append(num)
        sorted()
    
    # Return the sorted list
    return sorted_nums

# Test cases
test_cases = [ [ [1, 11, -1, -11, -12], [], 5] ]

# Call the function and check the output
for test_case in test_cases:
    actual_output = order_by_points(test_case)
    expected_output = [ -1, -11, 1, -12, 11 ]
    assert actual_output == expected_output, "Test case failed: " + str(test_case)

print("All tests passed!")
```