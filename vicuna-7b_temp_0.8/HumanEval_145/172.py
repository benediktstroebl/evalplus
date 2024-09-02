
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Check if the list is empty
    if not nums:
        return []
    
    # Get the sum of digits of the first number
    first_sum = sum([int(n) for n in nums[0]])
    
    # If the sum of digits is 0, the digits are not digested
    if first_sum == 0:
        return [nums]
    
    # Initialize a list to store the sorted list
    result = []
    
    # Loop through the list
    for num in nums:
        # Loop through the list of remaining numbers
        remaining_list = nums[1:]
        
        # While there are remaining numbers
        while remaining_list:
            
            # Find the number with the highest sum of digits
            max_num = None
            max_sum = 0
            for num in remaining_list:
                # Get the sum of digits of the current number
                digit_sum = sum([int(n) for n in str(num)])
                
                # Check if the current number has a higher sum of digits
                # than the current max number
                if digit_sum > max_sum or (digit_sum == max_sum and num < max_num):
                    # Update the max number and sum
                    max_num = num
                    max_sum = digit_sum
                    
            # Add the max number to the result list
            result.append(max_num)
            
            # Remove the max number from the remaining list
            num = max_num
            remaining_list = [x for x in remaining_list if x != num]
            
            # If there are no remaining numbers, add the current number to the result list
            if not remaining_list:
                result.append(num)
    
    # Return the sorted list
    return result