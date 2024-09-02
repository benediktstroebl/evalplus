
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0

    number_of_numbers = (10 ** n)

    start_with_1_count = 0
    end_with_1_count = 0

    for i in range(1, 10):
        start_with_1_count += i * number_of_numbers // 10

    end_with_1_count = (number_of_numbers // 10 - 1) * 9

    return start_with_1_count + end_with_1_count

