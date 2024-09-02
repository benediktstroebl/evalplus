
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # Split the integer into odd digits and even digits
    odd_digits, even_digits = [], []
    num = abs(num)
    while num > 0:
        odd_digits.append(num % 10)
        even_digits.append(num % 10)
        num //= 10

    # Count odd and even digits
    count_odd, count_even = 0, 0
    for d in odd_digits:
        if d % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    for d in even_digits:
        if d % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return (count_odd, count_even)
