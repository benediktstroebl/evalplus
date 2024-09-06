
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count the number of digits that are 1, but not 0
    digits = n + (n > 1)
    dig = 1
    count = 0
    # since we don't want to double count, we will need to remember the
    # last digit seen, and reset the count at each digit
    last_seen = -1

    while dig <= digits:
        # if current digit is 1, increment count
        if dig % 10 == 1:
            count += 1

        # save the last digit seen
        last_seen = dig % 10

        # increment dig before checking to see if last digit was 1, as it
        # may be 1 but not counted as last digit seen
        dig += 1

    # if last digit is 1, increment count
    if last_seen == 1:
        count += 1

    return count

