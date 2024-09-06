
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return even_odd_count(abs(num))
    else:
        num_of_even = 0
        num_of_odd = 0
        while num:
            if num % 2 == 0:
                num_of_even += 1
            else:
                num_of_odd += 1
            num /= 10
        return (num_of_even, num_of_odd)

