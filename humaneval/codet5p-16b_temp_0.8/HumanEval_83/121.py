
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    answer = 0
    
    def starts_one_ends_helper(digits):
        nonlocal answer
        if digits == 1:
            answer += 1
        else:
            starts_one_ends_helper(digits - 1)
            starts_one_ends_helper(1)
            starts_one_ends_helper(digits)
            
    starts_one_ends_helper(n)
    return answer
