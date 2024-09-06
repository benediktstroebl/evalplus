
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
    # Set the pivot as the largest digit in the list
    pivot = max(nums)
    
    # Loop through the list
    for num in nums:
        # Convert the number to its digit
        digit = sum(int(digit) for digit in str(num))
        
        # If the digit is greater than or equal to pivot, move it to the right
        if digit >= pivot:
            nums.remove(num)
            nums.insert(nums.index(num) + 1, num)
            nums.insert(0, pivot)
        else:
            # If the digit is less than pivot, move the digit to the right
            nums.insert(0, digit)
            nums.insert(nums.index(num) + 1, num)
    
    return nums