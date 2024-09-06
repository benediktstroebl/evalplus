
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 3 is the smallest number that ends with 1
    start_one_count = 3

    # if n is 1, then the count is 2
    if n == 1:
        end_one_count = 2
    else:
        # otherwise, use the recurrence relation to calculate the count
        end_one_count = (n//10) // 2 + start_one_count
        
    return start_one_count + end_one_count
