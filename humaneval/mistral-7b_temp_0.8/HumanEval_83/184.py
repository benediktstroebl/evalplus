
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    n_digits = len(str(n))
    one_count = 0
    for i in range(10**n_digits):
        if i < 10:
            if i == 1:
                one_count += 1
        elif i > 9 and i % 10 == 1:
            one_count += 1
        elif i // 10 % 10 == 1:
            one_count += 1
    return one_count

