
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # Base cases:
    if num < 0:
        num = -num
        num += 1 # negative number needs an extra +1 to get the correct number of digits.

    # Recursive cases:
    if num == 0:
        return (0, 0)
    elif num < 10:
        return (1, 0)
    else:
        num = num % 10
        count_even = even_odd_count(num // 10)[0]
        count_odd = even_odd_count(num // 10)[1]

        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return (count_even, count_odd)

