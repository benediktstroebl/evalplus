
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digit = 0
    while num > 0:
        if num % 10 == 0:
            digit += 1
        num /= 10
    return (digit, digit+1) if digit % 2 == 0 else (digit+1, digit)

num = int(input("Enter an integer: "))
