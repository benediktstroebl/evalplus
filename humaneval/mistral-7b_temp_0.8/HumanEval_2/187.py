

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    def truncate_number_aux(number: float, decimals: float) -> float:
        # Base case: if number is 0 or less than 1 return 0.
        if number <= 1:
            return 0
        # Divide number by 10 to convert decimals into integer.
        decimals = int(decimals * 10)
        # Calculate the integer part of the number.
        integer = number // 10
        # Calculate the remaining decimals.
        decimals = decimals - integer
        # Return the decimal part of the number.
        return decimals / 10

    return truncate_number_aux(number, number)

