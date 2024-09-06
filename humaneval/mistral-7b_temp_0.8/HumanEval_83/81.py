
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    answer = 0
    for i in range(1, n+1):
        answer += len(str(i)) * 2
        answer += len(str(i))
    return answer

