
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    m = len(str(n))
    answer = 0

    for i in range(pow(10, m-1), pow(10, m)):
        if str(i)[0] == '1':
            answer += 1

    for j in range(pow(10, m-1), pow(10, m)):
        if str(j)[-1] == '1':
            answer += 1

    return answer

