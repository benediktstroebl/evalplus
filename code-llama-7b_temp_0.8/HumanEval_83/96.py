
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    one_digit_cases = ["1", "9"]
    two_digit_cases = [
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "90",
        "91",
        "92",
        "93",
        "94",
        "95",
        "96",
        "97",
        "98",
        "99",
    ]
    if n == 1:
        return len(one_digit_cases)
    elif n == 2:
        return len(two_digit_cases)
    else:
        return len(one_digit_cases) + len(two_digit_cases) + starts_one_ends(
            n - 2
        )

