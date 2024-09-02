
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
    # [1, 11, -1, -11, -12]
    # 
    # [(-1, 2), (1, 1), (11, 2), (-11, 2), (-12, 2)]
    # 
    # [-1, -11, 1, -12, 11]

    # 1. Put a score for each integer
    # 2. Sort the list by score
    # 3. Sort the list by index
    # 4. return the sorted list

    # 1. Put a score for each integer
    scores = []
    for num in nums:
        score = sum([int(i) for i in str(num)])
        scores.append((num, score))

    # 2. Sort the list by score
    scores.sort(key=lambda x: x[1])

    # 3. Sort the list by index
    scores.sort(key=lambda x: nums.index(x[0]))

    # 4. return the sorted list
    return [x[0] for x in scores]
