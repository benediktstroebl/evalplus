

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    direction = 0  # 0: increasing, 1: decreasing, -1: changing

    for i in range(1, len(l)):
        # print(f'direction={direction}, l[i]={l[i]}')
        if direction == 0:
            if l[i] > l[i-1]:
                direction = 1
            elif l[i] < l[i-1]:
                direction = -1
        elif direction == 1:
            if l[i] < l[i-1]:
                return False
        elif direction == -1:
            if l[i] > l[i-1]:
                return False
    return True
