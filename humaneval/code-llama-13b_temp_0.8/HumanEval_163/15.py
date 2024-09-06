
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_int_list = []

    for i in range(a, b + 1):
        if str(i)[-1] == '0':
            even_int_list.append(i)
        elif str(i)[-1] == '2':
            even_int_list.append(i)
        elif str(i)[-1] == '4':
            even_int_list.append(i)
        elif str(i)[-1] == '6':
            even_int_list.append(i)
        elif str(i)[-1] == '8':
            even_int_list.append(i)
        elif str(i)[-1] == '1':
            continue
        elif str(i)[-1] == '3':
            continue
        elif str(i)[-1] == '5':
            continue
        elif str(i)[-1] == '7':
            continue
        elif str(i)[-1] == '9':
            continue

    return even_int_list

