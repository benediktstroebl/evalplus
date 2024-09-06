
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here

    # #One way to solve it
    # count = 0
    # for i in range(1, n+1):
    #     count += sum([int(x[0] == '1' or x[-1] == '1') for x in str(i).split()])
    # return count

    # # another way to solve it
    # s = ''.join(str(i) for i in range(1, n+1))
    # return s.count('1') + s.count('10')

    # fastest way to solve it
    return 2*sum(x in '10' for x in str(range(1, n+1)))
