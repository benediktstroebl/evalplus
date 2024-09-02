
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # clean data
    n = int(n)
    # math
    # first figure out how many even numbers will be needed
    # e.g. to make 8, two 2s and two 4s will do
    # then figure out if the other numbers will work
    # e.g. to make 8, 2 and 4 work, the other two numbers must be 2 and 2
    num_even_needed = n // 4
    remainder = n % 4
    if remainder != 0:
        return False
    # now we know how many even numbers to use in our sum
    # but do they have to be the same?
    # they do if the number of even numbers is odd
    # if the number of even numbers is even
    # then the even numbers can be different
    # they don't have to be the same if the number of even numbers is even
    if num_even_needed % 2 == 0:
        return True
    # they do if the number of even numbers is odd
    if num_even_needed % 2 == 1:
        return False
