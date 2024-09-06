
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    nums = list(arr)
    if not nums:
        return None
    positive_nums, negative_nums = [], []
    for num in nums:
        if num >= 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)
    positive_nums.sort()
    negative_nums.sort()
    positive_magnitudes = [num for num in positive_nums if num!= 0]
    negative_magnitudes = [num for num in negative_nums if num!= 0]
    result = sum(map(abs, positive_magnitudes))
    if negative_magnitudes:
        result *= negative_magnitudes[0]
        for num in negative_magnitudes[1:]:
            result *= num
    return result

