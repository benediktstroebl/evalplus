
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count = 0
    # for i in range(10):
    #     for j in range(10):
    #         if i != j:
    #             s = str(i) + str(j) + str(n-2)
    #             if s.startswith('1') or s.endswith('1'):
    #                 count += 1
    # return count
    return sum(1 for i in range(10) if str(i).startswith('1') or str(i).endswith('1'))
