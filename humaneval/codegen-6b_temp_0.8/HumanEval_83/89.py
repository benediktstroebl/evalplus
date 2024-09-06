
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_set = set(str(i) for i in range(10))
    num_set.add('1')

    def count_digit_one(n):
        count = 0

        for _ in range(n):
            if '1' in num_set:
                count += 1
            num_set.remove('1')

        return count

    return count_digit_one(n) + count_digit_one(n - 1)

