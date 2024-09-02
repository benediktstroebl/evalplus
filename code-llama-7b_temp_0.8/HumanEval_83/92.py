
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Get the number of 1-digit numbers that start or end with 1
    one_digit = 0
    if n == 1:
        one_digit = 2
    else:
        # Get the number of 2-digit numbers that start or end with 1
        two_digit = 0
        if n == 2:
            two_digit = 2
        else:
            # The total count of n-digit numbers that start or end with 1
            count = 0
            # The count of n-digit numbers that end with 1
            end_with_one = 1
            # The count of n-digit numbers that start with 1
            start_with_one = 1
            # The count of n-digit numbers that have the last digit 1
            one_at_the_end = 1
            # The count of n-digit numbers that have the first digit 1
            one_at_the_start = 1
            # The count of n-digit numbers that start or end with 1
            end_with_one += start_with_one
            end_with_one += one_at_the_end
            start_with_one += one_at_the_start
            count += end_with_one
            count += start_with_one
            for i in range(2, n):
                # The count of n-digit numbers that have the last digit 1
                one_at_the_end = one_at_the_end * 10 + 1
                # The count of n-digit numbers that have the first digit 1
                one_at_the_start = one_at_the_start * 10 + 1
                # The count of n-digit numbers that end with 1
                end_with_one += one_at_the_end
                # The count of n-digit numbers that start with 1
                start_with_one += one_at_the_start
                # The count of n-digit numbers that start or end with 1
                end_with_one += start_with_one
                end_with_one += one_at_the_start
                count += end_with_one
           
