

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Create a list of numbers from 1 to n.
    list_of_numbers = [i for i in range(1, n)]

    # Create two new empty lists.
    divisible_by_11 = []
    divisible_by_13 = []

    # Iterate over the list and store divisible by 11 and divisible by 13 numbers in the new lists.
    for number in list_of_numbers:
        if number % 11 == 0:
            divisible_by_11.append(number)
        if number % 13 == 0:
            divisible_by_13.append(number)

    # Get the length of the new lists.
    count_by_11 = len(divisible_by_11)
    count_by_13 = len(divisible_by_13)

    # Return the sum of the counts.
    return count_by_11 + count_by_13
