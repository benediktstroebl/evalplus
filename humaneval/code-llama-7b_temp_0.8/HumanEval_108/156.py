
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
    def get_first_positive_digit(number):
        if number < 0:
            return -number % 10
        else:
            return number % 10

    def get_next_digit(number):
        return number // 10

    result = 0
    for num in arr:
        sum_of_digits = 0
        number = abs(num)
        while number != 0:
            sum_of_digits += get_first_positive_digit(number)
            number = get_next_digit(number)
        result += int(sum_of_digits > 0)
    return result

