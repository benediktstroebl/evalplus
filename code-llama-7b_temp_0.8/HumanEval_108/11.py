
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
    def is_positive(number):
        return number > 0

    def is_negative(number):
        return number < 0

    def get_num(number):
        return number % 10

    def get_next_num(number):
        return number // 10

    def has_digit(number):
        if number < 10:
            return True
        else:
            return has_digit(get_next_num(number))

    def sum_digits(number):
        if number == 0:
            return 0
        if number < 0:
            return sum_digits(-number)
        return sum_digits(get_next_num(number)) + get_num(number)

    def count_nums_iter(arr):
        count = 0
        for number in arr:
            if is_negative(number):
                if has_digit(get_next_num(number)):
                    count += 1
            elif is_positive(number):
                if has_digit(number):
                    count += 1
        return count

    return count_nums_iter(arr)
