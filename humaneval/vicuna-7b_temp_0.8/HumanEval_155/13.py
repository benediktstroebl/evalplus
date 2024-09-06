
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digit_count = {}
    for i in range(10):
        digit_count[str(num)[i]] = digit_count.get(str(num)[i], 0) + 1
    for key in sorted(digit_count.keys()):
        digit_count[key] //= 2
    return digit_count.get(str(num)[0], (0, 0))
num = int(input("Enter a number: "))
