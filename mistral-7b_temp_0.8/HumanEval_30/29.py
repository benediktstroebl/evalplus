

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # 입력받은 리스트의 값을 하나씩 꺼내고, 그 값이 양수인 경우에만 그 값을 리스트에 추가하고, 더 이상 꺼내지 않을 때까지 반복한다.
    positive_nums = []
    for num in l:
        if num > 0:
            positive_nums.append(num)
    return positive_nums

