
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a dictionary to store the number of even digits in each number
    # We can't just use a list, because we need to be able to handle numbers like 99
    nums = {int(n) for n in str(n) if n in str(int(n))}
    if all(d%2 == 0 for d in nums):
        return 0
    else:
        # Calculate the product of the odd digits
        odd_digits = [d for d in nums if d%2 == 1]
        return sum(odd_digits)
