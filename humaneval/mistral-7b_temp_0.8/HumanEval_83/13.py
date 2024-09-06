
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    count = 0
    for i in range(10 ** n):
        if i == int(str(i)[-1]) or i == int(str(i)[0]):
            count += 1
    return count

