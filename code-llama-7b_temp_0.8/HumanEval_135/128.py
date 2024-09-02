
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # TODO: Write your solution here
    # 1. 开一个记录当前最大下标的数组，维护一个最小值，从左向右遍历，找到第一个比当前最小值大的值
    # 2. 维护一个记录当前最小值的数组
    # 3. 记录当前最大下标
    min_value = float("inf")
    min_value_index = None
    max_index = -1
    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_value_index = i
            max_index = i
        else:
            if arr[i] >= arr[max_index]:
                max_index = i
            else:
                max_index = min_value_index
    return max_index

