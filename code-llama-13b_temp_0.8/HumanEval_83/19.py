
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    count = 0
    for i in range(1, n):
        num = 10 ** (n - 1) + i
        if n == len(str(num)):
            count += 1
        elif str(num)[0] == '1' or str(num)[-1] == '1':
            count += 1

    return count
