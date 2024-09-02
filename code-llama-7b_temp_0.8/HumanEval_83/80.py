
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Cases:
    # 123456, 123456, ..., 123456
    # 12345, 12345, ..., 12345
    # 1234, 1234, ..., 1234
    # 123, 123, ..., 123
    # 12, 12, ..., 12
    # 1, 1, ..., 1

    # Do this in O(1) time
    # Can only count 1s if there is at least 1 in the number
    # Can only count 1s if there is at least 1 leading 1 (last position)
    # Can only count 1s if there are at least 2 leading 1s (first position)
    # Can only count 1s if there are at least 3 leading 1s (middle position)
    # Can only count 1s if there are at least 4 leading 1s (middle position)
    # Can only count 1s if there are at least 5 leading 1s (middle position)
    # Can only count 1s if there are at least 6 leading 1s (middle position)

    # Do this in O(1) space

    # O(1) Time
    # 1 digit numbers -> 6 possible cases
    # 2 digit numbers -> 12 possible cases
    # 3 digit numbers -> 24 possible cases
    # 4 digit numbers -> 48 possible cases
    # 5 digit numbers -> 96 possible cases
    # 6 digit numbers -> 192 possible cases

    # O(1) Space
    # Use a constant amount of space
    # 1 digit numbers -> 6 possible cases
    # 2 digit numbers -> 12 possible cases
    # 3 digit numbers -> 24 possible cases
    # 4 digit numbers -> 48 possible cases
    # 5 digit numbers -> 96 possible cases
    # 6 digit numbers -> 192 possible cases

    one_end = 0

    # For each
