
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Define helper function
    def helper(n):
        # If all digits are even, return 0
        if all(d % 2 == 0 for d in n):
            return 0
        # Loop through digits
        for d in n:
            # If loop breaks because all digits are odd, return product
            if all(d % 2 == 1 for d in n):
                return n[0]
            # Loop through digits
            for i in range(1, len(n)):
                # If loop breaks because all digits are even, return sum of remaining digits
                if all(d % 2 == 0 for d in n[:i+1]):
                    return sum(n[:i+1])
                # Loop through digits
                for j in range(i+1, len(n)):
                    # If loop breaks because all digits are odd, return product of remaining digits
                    if all(d % 2 == 1 for d in n[:j+1]):
                        return n[j] * n[j+1]
                    # Loop through digits
                    for k in range(j+2, len(n)):
                        # If loop breaks because all digits are even, return sum of remaining digits
                        if all(d % 2 == 0 for d in n[:k+1]):
                            return sum(n[:k+1])
                        # Loop through digits
                        for l in range(k+2, len(n)):
                            # If loop breaks because all digits are odd, return product of remaining digits
                            if all(d % 2 == 1 for d in n[:l+1]):
                                return n[k] * n[l]
                            # Loop through digits
                            for m in range(l+2, len(n)):
                                # If loop breaks because all digits are even, return sum of remaining digits
                                if all(d % 2 == 0 for d in n[:m+1]):
                                    return sum(n[:m+1])
                                # Loop through digits
                                for o in range(m+2, len(n)):
                                    # If loop breaks because all digits are odd, return
