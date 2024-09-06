def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Returns an empty list if the input list is empty.

    """
    if not nums:
        return []

    # Calculate the digit-sum-sorted index list
    ds_idxs = [
        (sum(int(d).digits()), i) 
        for i, d in enumerate(nums) 
    ]
    ds_idxs.sort()
    
    # Use the sorted index list to construct the sorted digit-sum list
    sorted_nums = [nums[i] for i, _ in ds_idxs]

    return sorted_nums