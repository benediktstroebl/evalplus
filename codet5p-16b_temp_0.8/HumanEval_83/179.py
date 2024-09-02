
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def get_starts_ends(n):
        starts = 0
        ends = 0
        for i in range(1, 10**n):
            num = str(i)
            if num[0] == '1':
                starts += 1
            if num[-1] == '1':
                ends += 1
        return starts, ends
    
    starts, ends = get_starts_ends(n)
    return starts + ends

