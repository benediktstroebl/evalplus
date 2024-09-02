
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 对象
    n = len(lst)
    # 忽略环境变量
    for i in range(n):
        if lst[i] % 2 == 0:
            # 判断数是否奇偶
            if lst[i] % 2 == 1:
                # 如果是奇数，就将数字从后面移动一格
                j = i + 1
                while lst[j] % 2 == 0:
                    j += 1
                # 将数字从第 i 坐标移动到第 j 坐标
                lst[i:j] = lst[i:j] + [lst[i]]
    return sum(lst)
