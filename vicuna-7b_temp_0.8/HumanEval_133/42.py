

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    # 根据元数据找到左右边的两个元素的乘积
    left_sum = 0
    right_sum = 0
    # 检查lst的长度是否为1
    if len(lst) == 1:
        return lst[0]**2
    for num in lst:
        if num >= 0:
            left_sum += num
        elif num < 0:
            right_sum -= num
        else:
            left_sum += 2*(num**2)
            right_sum += 2*(num*-1)
    return round(left_sum+right_sum,2)