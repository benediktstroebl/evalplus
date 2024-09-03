def order_by_points(nums):
    # Convert list of integers into list of digits
    nums_list = [int(num) for num in nums]
    
    # Sort the list of digits
    return sorted(nums_list, key=lambda x: sum(int(str(x))))
nums = [1, 11, -1, -11, -12]