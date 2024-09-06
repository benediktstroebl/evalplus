
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n==1:
        return 0
    start_count = 0
    end_count = 0
    for x in range(10):
        if x==0:
            start_count += 1
        elif x==9:
            end_count += 1
        elif x==1:
            start_count += ends_one(n-1)
            end_count += starts_one(n-1)
        else:
            start_count += starts_one(n-1)
            end_count += ends_one(n-1)
    return start_count + end_count

