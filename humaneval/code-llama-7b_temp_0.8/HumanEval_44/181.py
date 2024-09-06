

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # 将整数x转化为字符串形式
    x_str = str(x)

    # 将x转化为字符串的数字列表
    x_list = [int(char) for char in x_str]

    # 定义一个空列表来存储结果
    result_list = []

    # 定义一个标记位，用来判断输入的x是否为0
    is_zero = True

    for num in x_list:
        # 判断输入的x是否为0
        if num != 0:
            is_zero = False

    # 计算将x转化为输入的base的过程
    if is_zero:
        return '0'
    else:
        for i in x_list:
            # 把每个数字除以base，并将余数存储到result_list中
            result_list.append(i % base)
            # 将余数除以base
            i //= base

        # 定义一个字符串变量，来存储转化后的字符串
        result_str = ''

        # 遍历result_list，取出每个元素，并将其转化为str类型
        for item in reversed(result_list):
            result_str += str(item)
        return result_str

