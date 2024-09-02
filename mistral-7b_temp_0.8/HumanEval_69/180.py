
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
    # 创建一个字典
    dic = {}
    # 遍历元素
    for i in lst:
        # 如果字典中没有值，则添加值
        if i not in dic:
            dic[i] = 1
        # 如果字典中有值，则添加数量
        else:
            dic[i] += 1
    # 循环遍历字典，如果字典中有值大于等于对应的数量，则返回字典中的数量
    for j in dic.keys():
        if dic[j] >= j:
            return j
    return -1
