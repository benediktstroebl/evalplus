
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # If the range is empty, return an empty list
    if a > b:
        return []

    # Split the range into two parts
    a_parts = [a]
    b_parts = [b]

    # Loop through the parts
    for i, part in enumerate(a_parts):
        # Loop through the parts again, this time stepping by 2
        for j in range(i + 1, len(b_parts) - 1):
            b_parts[j] = part * 2 + b_parts[j - i - 1]

    # Filter the parts to keep only the even digits
    even_parts = [i // 2 for i in b_parts]

    # Return the filtered parts
    return even_parts
