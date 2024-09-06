```python
def double_the_difference(nums):
    """
    Sum of squares of odd integers in a list given.
    
    Args:
        nums (list): List of numbers
    
    Returns:
        int: Sum of squares of odd integers or 0 if no such integers in the list
    """
    ans = 0
    for n in nums:
        if isinstance(n, int) and n > 0 and n % 2:
            ans += n * n
    return ans

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
print(double_the_difference([0]))  # Output: 0
print(double_the_difference([]))  # Output: 0
```

This script provides a function called `double_the_difference`. This function takes a list of numbers as input and returns the sum of the squares of odd numbers in the list. The function checks if each number is an integer and greater than zero, and if so, it checks if the number is odd to determine if it should be squared and added to the total. The function returns 0 if the input list is empty or if there are no odd integers in the list.

The test cases provided return the expected outputs based on the given criteria and populate them to the console for verification.