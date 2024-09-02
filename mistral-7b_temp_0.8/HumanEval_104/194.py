
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

    ## 1.
    # 创建一个空列表，用来存储符合条件的数字
    result_list = []
    # 遍历所有数字
    for i in x:
        # 如果数字中不包含偶数
        if len(set(str(i)).intersection(set(range(2,10)))) == 0:
            # 将数字添加到结果列表中
            result_list.append(i)
    # 返回结果列表
    return sorted(result_list)


    ## 2.
    # 创建一个空列表，用来存储符合条件的数字
    result_list = []
    # 遍历所有数字
    for i in x:
        # 如果数字中不包含偶数
        if set(str(i)).issubset(set(range(2,10))):
            # 将数字添加到结果列表中
            result_list.append(i
