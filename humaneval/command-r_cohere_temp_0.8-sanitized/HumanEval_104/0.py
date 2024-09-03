def unique_digits(x):
    """Returns a sorted list of elements with unique digits from the given list of positives.

    Args:
        x (list): A list of positive integers.

    Returns:
        list: A sorted list of integers with unique digits.
    """
    result = []
    for num in x:
        has_even_digit = any(int(char) % 2 == 0 for char in str(num))
        if not has_even_digit:
            result.append(num)
    result.sort()
    return result