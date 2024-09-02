
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < 1 or y < 1:
        return -1

    even_nums = []
    even_num = 0

    while even_num <= y:
        if even_num % 2 == 0:
            even_nums.append(even_num)
        even_num += 1

    for num in even_nums:
        if num >= x and num <= y:
            return num

    return -1
    






