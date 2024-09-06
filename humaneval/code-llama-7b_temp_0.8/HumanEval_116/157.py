
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
    num_list = [None] * len(arr)
    count_one_dict = {}
    for i in range(len(arr)):
        num = arr[i]
        count_one = bin(num).count("1")
        if count_one not in count_one_dict:
            count_one_dict[count_one] = [num]
        else:
            count_one_dict[count_one].append(num)

    count_one_list = [key for key in count_one_dict.keys()]
    count_one_list.sort()
    for i in range(len(arr)):
        one_count = count_one_list[i]
        num_list[i] = min(count_one_dict[one_count])
        count_one_dict[one_count].remove(min(count_one_dict[one_count]))

    return num_list

