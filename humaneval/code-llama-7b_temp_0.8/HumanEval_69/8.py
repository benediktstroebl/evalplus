
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # 考虑到其中的键可能会有重复，所以使用字典来保存键及其频率
    # 第一个元素是被选中的元素，所以其频率为1
    dct = {lst[0]: 1}
    # 遍历原列表
    for num in lst[1:]:
        # 如果其频率小于等于当前数值，则将其频率增加
        if dct[num] <= num:
            dct[num] += 1
        # 如果其频率大于当前数值，则将当前数值赋值给第一个元素
        else:
            lst[0] = num
    # 遍历字典，找到频率大于当前数值的最小的元素
    for num in dct:
        if num > lst[0]:
            lst[0] = num
    # 如果没有符合的元素，返回-1
    if lst[0] == lst[1]:
        lst[0] = -1
    return lst[0]

