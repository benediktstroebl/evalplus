
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    """
    my_list = []
    for num in arr:
        temp = sum(int(char) for char in str(num))
        if temp > 0:
            my_list.append(num)
    print(my_list)
    return len(my_list)
    """
    new_list = [abs(num) for num in arr]
    print(new_list)
    return sum(sum(int(char) for char in str(num)) > 0 for num in new_list)
