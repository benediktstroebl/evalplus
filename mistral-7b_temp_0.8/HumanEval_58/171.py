

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    def merge_sort(l):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        return merge(
            merge_sort(l[:mid]),
            merge_sort(l[mid:])
        )

    def merge(l1, l2):
        l1_i, l2_i = 0, 0
        result = []
        while l1_i < len(l1) and l2_i < len(l2):
            if l1[l1_i] < l2[l2_i]:
                result.append(l1[l1_i])
                l1_i += 1
            else:
                result.append(l2[l2_i])
                l2_i += 1
        if l1_i == len(l1):
            result += l2[l2_i:]
        else:
            result += l1[l1_i:]
        return result

    l1, l2 = merge_sort(l
