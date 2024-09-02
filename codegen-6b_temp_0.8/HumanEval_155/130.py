
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    negative = (num < 0)
    num = abs(num)

    num_list = []
    count = 0
    while num > 0:
        num_list.append(num % 10)
        num /= 10
        count += 1

    odd_count = len(num_list) - num_list.count(0)
    if negative:
        odd_count *= -1

    if count % 2 == 0:
        return (odd_count, count - odd_count)
    else:
        return (count - odd_count, odd_count)

