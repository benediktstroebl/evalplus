

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def is_fizz(num):
        """Return True if num is divisible by 11, else False."""
        return num % 11 == 0
    
    def is_buzz(num):
        """Return True if num is divisible by 13, else False."""
        return num % 13 == 0
    
    for i in range(n):
        if is_fizz(i):
            print(i, end=" ")
        else:
            print(i, end=" ")
        if is_buzz(i):
            print("7", end=" ")
        else:
            print(i, end=" ")
    print()
