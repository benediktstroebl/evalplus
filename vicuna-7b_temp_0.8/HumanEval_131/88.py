
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Convert n to string and reverse it
    n_str = str(n)
    n_rev = n_str[::-1]
    
    # Check if all digits are even
    if sum(int(n_rev) for n_rev in n_str) % 2 == 0:
        return 0
    
    # Calculate the product of the odd digits
    odd_digits = [int(n_rev) for n_rev in n_str if n_rev.isdigit() and int(n_rev) % 2 != 0]
    return reduce(mul, odd_digits, 1)
