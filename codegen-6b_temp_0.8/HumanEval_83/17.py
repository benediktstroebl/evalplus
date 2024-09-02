
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 3
    if n == 2:
        return 1
    if n == 3:
        return 1
    def counts(n):
        # numbers with n digits, beginning or ending with 1
        if n == 1:
            return 3
        if n == 2:
            return 1
        if n == 3:
            return 1
        def starts(n):
            if n == 0:
                return 1
            if n == 1:
                return 2
            if n == 2:
                return 2
            def ends(n):
                if n == 0:
                    return 1
                if n == 1:
                    return 2
                if n == 2:
                    return 1
                def starts_one(n):
                    if n == 1:
                        return 3
                    if n == 2:
                        return 2
                    if n == 3:
                        return 1
            return starts_one(n) + ends(n - 2)
        return counts(n - 1) + starts(n)
    return counts(n)
