
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    total_even = 0
    total_odd = 0

    num_str = str(abs(num))
    if len(num_str) > 1 and num_str[0] == "0":
        num_str = num_str[1:]

    for digit in num_str:
        if int(digit) % 2 == 0:
            total_even += 1
        else:
            total_odd += 1

    return (total_even, total_odd)

