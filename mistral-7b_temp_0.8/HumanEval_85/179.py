
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    nums = []
    for i in range(len(lst)):
        if i % 2 != 0:
            nums.append(lst[i])
    nums.sort()
    sum = 0
    for num in nums:
        sum += num
    return sum


