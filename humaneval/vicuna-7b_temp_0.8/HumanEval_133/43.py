

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
    # 数组sum 做归并运算 
    nums = sorted(lst)  # 将数组按值从小到大排序
    nums = [int(x) for x in nums]  # 将元素转化为整数
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i] = math.pow(nums[i], 2) + math.pow(nums[j], 2)  # 对数组进行归并运算
    return round(sum(nums), 0)  # 对结果进行几何运算

