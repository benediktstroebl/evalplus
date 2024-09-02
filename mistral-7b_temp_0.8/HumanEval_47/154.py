

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # TODO: Implement median.
    # Add your code here.

    # for i in range(1, len(l), 2):
    #     l.insert(0, l.pop())
    # return l[len(l) // 2]

    # 1. 将原来的数列进行排序
    # 2. 判断数列长度是奇数还是偶数
    # 3. 将数列长度除以2，并向下取整
    # 4. 如果数列长度是奇数，返回中间的那个数
    # 5. 如果数列长度是偶数，则取中间两个数的平均数
    l = sorted(l)
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

