
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
    # A dictionary is a built-in Python data structure that maps keys to values.
    # In this case, we use a dictionary to keep track of the number of positive
    # digits in each number.
    num_dict = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

    # We iterate over the numbers in the input list.
    for num in arr:
        # We add up the digits of the number, and store the result in a variable.
        digit_sum = sum(map(int, num))

        # We look up the number of positive digits in the dictionary and
        # increment it if the sum of the digits is positive.
        num_pos_digits = num_dict[digit_sum]
        num_pos_digits += 1
        num_dict[digit_sum] = num_pos_digits

    return len(num_dict)
