
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a_str = str(a)
    b_str = str(b)
    a_list = list(a_str)
    b_list = list(b_str)

    if a_list[0] == '0' or b_list[0] == '0':
        return []

    a_last_digit = int(a_list[-1])
    b_last_digit = int(b_list[-1])

    if a_last_digit == b_last_digit:
        # if they are the same, get the even numbers between the integers
        a_list.remove(a_list[-1])
        b_list.remove(b_list[-1])

        a_str = "".join(a_list)
        b_str = "".join(b_list)
        a = int(a_str)
        b = int(b_str)

        list_of_ints = []
        while a <= b:
            if a % 2 == 0:
                list_of_ints.append(a)
            a += 1
        return list_of_ints
    else:
        # if they are different, get the even numbers between a and
        # the last digit of b, and the even numbers between the first digit
        # of a and b
        a_str = "".join(a_list)
        b_str = "".join(b_list)
        a = int(a_str)
        b = int(b_str)

        first_even_list = []
        last_even_list = []

        # get all the even numbers between a and b
        while a <= b:
            if a % 2 == 0:
                list_of_ints.append(a)
            a += 1

        # get all the even numbers between a and the last digit of b
        while a <= b_last_digit:
            if a % 2 == 0:
                last_even_list.append(a)
            a += 1

        # get all the even numbers between the first digit of a and b
        a = int(a_list[0
