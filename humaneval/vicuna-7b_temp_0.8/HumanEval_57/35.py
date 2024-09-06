

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def merge_sort(l):
        if len(l) <= 1:
            return l
        else:
            m = len(l) // 2
            l_left, l_right = merge_sort(l[:m]), merge_sort(l[m:])
            return merge_sort(l_left) and merge_sort(l_right)

    def merge_recursive(l):
        if len(l) == 1:
            return l[0]
        else:
            m = len(l) // 2
            l_left = merge_recursive(l[:m])
            l_right = merge_recursive(l[m:])
            return merge(l_left, l_right)

    def merge(a, b):
        if a < b:
            return a
        else:
            return b

    left, right = merge_sort([], 0), merge_sort([], 0)
    l = merge(left, right)
    while len(l) > 0:
        if l[-1] < l[0]:
            l.pop()
        else:
            l.pop()
    return l