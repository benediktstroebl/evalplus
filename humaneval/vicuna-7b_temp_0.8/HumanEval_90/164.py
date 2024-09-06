
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # 判断列表是否为空
    if not lst:
        return None
    
    # 如果列表中没有第二个小于等于第一个元素的元素，返回None
    if lst[0] <= lst[1]:
        return None
    
    # 找到第二个小于等于第一个元素的元素
    i = 1
    while lst[i] >= lst[i-1]:
        i += 1
    return lst[i]
