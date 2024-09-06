
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 定义一个空列表，用来保存存在奇偶位置的奇数
    odd_pos = []
    for i in range(len(lst)-1):
        if lst[i] % 2 == 0:
            odd_pos.append(i+1)
    for i in odd_pos:
        # 如果当前偶位的数是奇数，则加上
        if lst[i] % 2 != 0:
            odd_pos.remove(i)
            lst.remove(lst[i])
            i = i - 1
            while lst[i] % 2 == 0:
                i -= 1
            odd_pos.append(i+1)
    return sum(lst)
