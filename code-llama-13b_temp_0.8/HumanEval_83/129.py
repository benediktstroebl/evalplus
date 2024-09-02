
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # your code here
    count = 0
    for i in range(n):
        # print('i', i)
        if i == 0 or i == n-1:
            if i == 0:
                num = 1
            else:
                num = int(str(n) + str(1))
            for j in range(1, n):
                num *= 10
            count += num
            print('num', num)
            print('count', count)
        else:
            count += 9 * 10**(n-1)
    return count

