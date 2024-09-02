

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if n == 0:
        return "0"
    def count_to_string(n: int) -> str:
        if n == 0:
            return ""
        elif n == 1:
            return " "
        else:
            return count_to_string(n - 1) + " " + str(n)
    return count_to_string(n)

