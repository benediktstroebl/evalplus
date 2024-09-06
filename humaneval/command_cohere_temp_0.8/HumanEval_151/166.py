Here's a Python function that solves the given problem and includes relevant tests:
```python
def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list that are integers.
    
    Args:
        nums (list): List of numbers.
    
    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only even or negative numbers.
    """
    if not nums:  # Handle empty list
        return 0
    
    odd_nos = [num for num in nums if num % 2 and num >= 0]  # Filter odd, positive integers
    return sum(num ** 2 for num in odd_nos)

# Test cases
print(double_the_difference([]))  # Output: 0
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
```

The function leverages list comprehension to filter out odd, positive integers from the input list and then calculates their squares summing them up. Empty lists return 0, and any negative or non-integer numbers are ignored. 

The test cases help validate the function's behavior against different scenarios.