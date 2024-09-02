
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    num_list = []
    # TODO: Write your solution here
    if a > b:
        for num in range(b,a+1,2):
            num_list.append(num)
    else:
        for num in range(a,b+1,2):
            num_list.append(num)
    return num_list
