
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def count_digits(number):
        count = 0
        while number != 0:
            number = number // 10
            count += 1
        return count

    even_count = count_digits(num) - count_digits(abs(num) % 10)
    odd_count = count_digits(abs(num) % 10)
    return even_count, odd_count

