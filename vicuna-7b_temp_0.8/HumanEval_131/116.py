
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Helper function
    def helper(n):
        # Check if all digits are even
        if sum(n) % 2 == 0:
            return 0
        # Extract the odd digits
        return [int(n % d) for d in range(10, len(str(n))) if d % 2 == 1]
    # Recursive solution
    return helper(n-1) * helper(n//10)
