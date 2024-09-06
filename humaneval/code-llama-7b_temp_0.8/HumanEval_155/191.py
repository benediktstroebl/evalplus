
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def is_even(num):
        return num % 2 == 0
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for digit in num_str:
        if is_even(int(digit)):
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

