
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # your code here
    # 1. 整数を辞書に書き込む
    # 2. 辞書から0以上の値のみを取り出す
    # 3. 数字をリストに変換して返す
    nums = {}
    for x in x:
        nums[x] = 0
    nums = list(filter(lambda x:x[1] > 0, nums.items()))
    return list(map(lambda x:x[0], nums))
