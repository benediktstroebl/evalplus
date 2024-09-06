
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    answer = 0
    number = str(n)
    nums = [int(i) for i in number]
    for i in nums:
        if i == 1:
            answer += 1
    return answer
