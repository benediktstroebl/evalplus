
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # create a list with all numbers with 3 digits
    num_list = list(range(100,1000))

    # define a function that checks the first digit
    def first_digit(num):
        first = num // 100
        return first

    # define a function that checks the last digit
    def last_digit(num):
        last = num % 10
        return last

    # add up the number of numbers that start or end with 1
    count = sum(x for x in num_list if first_digit(x) == 1 or last_digit(x) == 1)
    return count
