Here's a Python script with a self-contained function that solves the problem and includes helpful messages when the function is called with the various test cases:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result

# Test cases
print(f"Test case 1: {double_the_difference([1, 3, 2, 0]) == 10}")
print(f"Test case 2: {double_the_difference([-1, -2, 0]) == 0}")
print(f"Test case 3: {double_the_difference([9, -2]) == 81}")
print(f"Test case 4: {double_the_difference([0]) == 0}")
print(f"Test case 5: {double_the_difference([]) == 0}")
```

This script provides a function that solves the problem, and for each test case, it prints out a message indicating whether the function's result matches the expected output. 

To run this script, you can either copy the test cases into separate cells in a Python environment, or modify the script to use those cases as input (e.g., reading inputs from a CSV file or prompting the user for input). 

Please let me know if you'd like to see the script formatted differently or structured in a way that better suits your needs!