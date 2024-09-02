
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Lets create a helper function to help us with this
    def get_even_odd_count_helper(num, even_count, odd_count):
        if num <= 0:
            return (even_count, odd_count)
        if num % 2 == 0:
            return get_even_odd_count_helper(num // 2, even_count + 1, odd_count)
        else:
            return get_even_odd_count_helper(num // 2, even_count, odd_count + 1)

    return get_even_odd_count_helper(num, 0, 0)

