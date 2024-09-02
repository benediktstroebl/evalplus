
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # a <= b
    if a > b:
        a, b = b, a

    # get range
    range_num = b - a

    # make even numbers
    even_nums = [num for num in range(a, b + 1, 2)]

    # check even numbers and range
    if not even_nums:
        return []

    # check range
    if range_num < 2:
        return even_nums

    # get numbers between
    range_num = range_num - 2

    # get start range
    start = even_nums[0]

    # get end range
    end = even_nums[-1]

    # get even numbers in between
    mid_even_nums = [num for num in range(start + 2, end, 2)]

    # append even numbers
    even_nums = even_nums + mid_even_nums

    # append start number
    even_nums.insert(0, start)

    # append end number
    even_nums.append(end)

    # return sorted list
    return sorted(even_nums)
