
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    arr = [i for i in arr if i > 0]
    result = []
    for num in arr:
        count = 0
        while num > 0:
            count += 1
            num = num // 2
        result.append(count)
        result.append(num)
    return result

@parser.add("Sort an array of non-negative integers using selection sort algorithm")
