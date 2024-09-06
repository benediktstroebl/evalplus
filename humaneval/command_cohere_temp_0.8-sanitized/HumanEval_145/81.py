def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Enumerate the list to have access to the original index during sorting
    enumerate_nums = list(enumerate(nums))
        
    # Sort function according to the sum of digits and original index
    def digit_sum_sort_key(num):
        # Get the sum of digits
        digit_sum = sum(map(int, str(num)))
        # Return a sorting key
        return (digit_sum, int(num))

    # Sort the list based on the sorting key
    sorted_enumerate_nums = sorted(enumerate_nums, key=digit_sum_sort_key)

    # Remove the enumeration and return the sorted list
    return [val[1] for val in sorted_enumerate_nums]