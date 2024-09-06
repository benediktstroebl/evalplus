

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return int(str(n).replace('7', '3')
       .replace('3', '7')
       .replace('11', '13')
       .replace('13', '11')
       .count('3')
    
