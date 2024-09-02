
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    n_str = str(n)
    n_str_len = len(n_str)

    def count_start_end_1(digits, start_end):
        if digits < 1:
            return 0

        start = start_end[0] * digits
        end = start_end[1] * digits

        if start_end == "start":
            return count_start_end_1(digits - 1, "end") \
               + int(n_str[:digits] == str(start) and n_str_len >= digits)
        elif start_end == "end":
            return count_start_end_1(digits - 1, "start") \
               + int(n_str[:digits] == str(end) and n_str_len >= digits)
        else:
            return count_start_end_1(digits - 1, "start") \
               + count_start_end_1(digits - 1, "end")

    return count_start_end_1(n_str_len, "start
