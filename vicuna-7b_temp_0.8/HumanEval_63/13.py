

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    # 创建空串
    str = []
    while n > 0:
        # 如果当前节点是空串，就当前节点为空串的长度，否则当前节点为空串的长度加上1
        if not str:
            fibfib_length = 1
        else:
            fibfib_length = int(str[-1]) + 1
        # 根据当前节点的长度计算下一个节点的长度
        n_len = n - fibfib_length
        # 将当前节点的长度和下一个节点的长度相加，并将结果添加到空串中
        str.append(n_len)
        n = fibfib_length
    # 返回最后一个节点的长度
    return str[-1]