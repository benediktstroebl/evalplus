
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # your code here
    # 將 x 到 y 間的數字取出來
    list_num = [num for num in range(x, y+1)]

    # 如果 list_num 裡沒有偶數的話，回傳 -1
    if not [num for num in list_num if num % 2 == 0]:
        return -1
    else:
        # 找到偶數中最大的那個
        return sorted([num for num in list_num if num % 2 == 0])[-1]

