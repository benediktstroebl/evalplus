
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

    count = 0
    for element in arr:
        if element > 0:
            string = str(element)
            sum = 0
            for letter in string:
                sum += int(letter)
            if sum > 0:
                count += 1
    return count
