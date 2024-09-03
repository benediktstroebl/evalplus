def order_by_points(nums):
    """
    Sort the list of integers by the sum of their digits and their original index.
    """
    nums_with_scores = [(sum(int(d) for d in str(num)), nums.index(num), num) for num in nums]
    nums_with_scores.sort()
    return [num for _, _, num in nums_with_scores]