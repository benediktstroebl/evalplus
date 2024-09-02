
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    num_list = list(str(n))

    if len(num_list) == 1:
        return 1

    for i in range(len(num_list)):
        if num_list[i] == '1':
            num_list.pop(i)
            count += int(int(''.join(num_list)) * (9 * 10 ** (len(num_list) - 1)))
            num_list.insert(i, '1')

    return count

