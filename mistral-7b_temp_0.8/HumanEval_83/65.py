
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Your code here
    count = 0

    if n == 0:
        return 1

    if n == 1:
        return 1

    for i in range(10):
        #print(i)
        count += 1
        if n > 1 and i == 0:
            count += 2
        elif n > 1:
            count += 1
    #print(count)

    return count


