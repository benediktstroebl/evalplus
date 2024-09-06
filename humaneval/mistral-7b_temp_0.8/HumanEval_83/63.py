
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    answer = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if i == j:
                answer += 1
            else:
                answer += 2
    return answer
