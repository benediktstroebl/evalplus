
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def count_digits(x):
        count = 0
        while x > 0:
            if x % 2 == 0:
                count += 1
            x = int(x / 2)
        return count

    def count_digits_from_to(from_, to):
        count = 0
        from_ = int(from_)
        to = int(to)
        while from_ <= to:
            count += count_digits(from_)
            from_ = int(from_ * 2)
        return count

    c = count_digits_from_to(a, b)
    return [c]
