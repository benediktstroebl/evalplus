
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # 将n的后半作为随机数生成
    random_num = int(n/2)
    # 将n的前半作为奇偶表示
    is_odd = n % 2 == 0
    # 生成每个层次的总数
    total_nums = [random_num]
    # 每个层次的数量
    nums = [total_nums[i] for i in range(1, len(total_nums))]
    # 返回每个层次的数量
    return nums
