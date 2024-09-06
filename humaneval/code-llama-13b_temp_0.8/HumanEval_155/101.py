
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # find negative or positive
    negative = 0
    positive = 0
    if num < 0:
        negative = 1
    if num > 0:
        positive = 1
    
    # count odds and evens
    num_str = str(abs(num))
    num_len = len(num_str)
    odds = 0
    evens = 0
    for i in range(num_len):
        if int(num_str[i]) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return (evens, odds)
