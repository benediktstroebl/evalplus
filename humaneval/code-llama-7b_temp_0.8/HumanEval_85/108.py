
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # 方法一：
    # i = 0
    # ans = 0
    # while i < len(lst):
    #     if i % 2 == 1:
    #         ans += lst[i]
    #     i += 1
    # return ans

    # 方法二：
    return sum(lst[i] for i in range(1, len(lst), 2))

