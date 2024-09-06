
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    evens_list = []

    # check for edge case where range is reversed
    if a > b:
        a, b = b, a

    for num in range(a, b + 1):
        string_num = str(num)

        for char in string_num:
            if char.isdigit():
                if int(char) % 2 == 0:
                    evens_list.append(int(char))

    return sorted(list(set(evens_list)))

