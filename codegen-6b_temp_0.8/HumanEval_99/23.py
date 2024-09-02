
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    numbers = [int(num) for num in value.split(",")]
    new_values = []

    for num in numbers:
        if num < 0:
            new_values.append(abs(num))
        else:
            new_values.append(num)

    numbers = new_values

    len_all_numbers = len(numbers)
    num_range = 100
    closest_num = None
    closest_num_index = None

    for i in range(len_all_numbers):
        first_num = numbers[i]
        first_num_index = i

        for j in range(i, len_all_numbers, 1):
            second_num = numbers[j]
            second_num_index = j

            for k in range(j, len_all_numbers, 1):
                third_num = numbers[k]
                third_num_index = k

                if abs(first_num - second_num) < num_range:
                    num_range = abs(first_num - second_num)
                    closest_num = first_num
                    closest_num_index = first_num_index

                elif abs(first_num - third_num) < num_range:
                    num_range = abs(first_num - third_num)
                    closest_num = first_num
                    closest_num_index = first_num_index

                elif abs(second_num - third_num) < num_range:
                    num_range = abs(second_num - third_num)
                    closest_num = second_num
                    closest_num_index = second_num_index
    return "%i" % closest_num


