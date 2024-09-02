

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    def partition(l: list, left: int, right: int):
        pivot = l[left]
        i = left + 1
        j = right
        while True:
            while l[i] < pivot: i += 1
            while l[j] >= pivot: j -= 1
            if i > j:
                break
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        l[left], l[j] = l[j], l[left]
        return j

    def quicksort(l: list, left: int, right: int):
        if left >= right: return
        pos = partition(l, left, right)
        quicksort(l, left, pos - 1)
        quicksort(l, pos + 1, right)

    quicksort(l, 0, len(l) - 1)
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2] + l[n // 2 - 1]) / 2.0
    else:
        return l[n // 2]

