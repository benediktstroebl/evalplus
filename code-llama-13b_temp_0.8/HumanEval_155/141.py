
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def even_odd_count_helper(num):
        if num < -10 or num > 10:
            return even_odd_count_helper(num // 10), even_odd_count_helper(num % 10)
        else:
            return 0, 1 if num & 1 else 1, 0
    return even_odd_count_helper(num)
