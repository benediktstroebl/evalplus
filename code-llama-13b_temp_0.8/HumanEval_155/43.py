
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_of_evens = 0
    count_of_odds = 0

    for i in str(num):
        if int(i) % 2 == 0:
            count_of_evens += 1
        else:
            count_of_odds += 1

    return count_of_evens, count_of_odds
