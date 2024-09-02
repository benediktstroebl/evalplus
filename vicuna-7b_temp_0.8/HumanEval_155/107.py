
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = [str(num)[i] if i % 2 == 0 else '0' for i in range(len(str(num))) if i % 2 == 0]
    if digits[-1] == '0':
        digits.pop()
    num_evens = sum(1 for d in digits if d == '0')
    num_odds = sum(1 for d in digits if d != '0')
    return num_evens, num_odds
