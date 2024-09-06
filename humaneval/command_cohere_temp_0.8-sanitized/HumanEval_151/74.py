def double_the_difference(nums):
    "Returns the sum of squares of odd integers in nums, handling invalid cases."
    # Validate input: nums is a list of integers
    if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums):
        return "Invalid input"
    
    # Handle empty list case
    if not nums:
        return 0
    
    # Filter odd and positive integers, double and sum them
    return sum(n ** 2 for n in nums if n % 2 == 1 and n >= 0)