def order_by_points(nums):
    # Initialize empty list to store the result
    result = []

    # Sort the list according to the sum of their digits in ascending order
    for num in nums:
        digit_sum = sum(int(c) for c in str(num))
        result.append(digit_sum)  # Add the digit sum to the result list

    return result  # Return the sorted list