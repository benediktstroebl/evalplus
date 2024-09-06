
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Avoid creating the same object many times in a loop.
    # This saves memory, but also speeds up the execution.
    a, b = abs(a), abs(b)
    numbers = []

    # While a is less than or equal to b.
    # Convert a to an integer.
    a_int = int(a)
    while a_int <= b:
        # Add 1 to a and b at the same time.
        a_int += 1
        b_int = int(b)
        # Append the digit of a to the list of numbers.
        numbers.append(a_int % 10)
        # If b is greater than a, b_int is also greater than 10.
        # In this case, b_int is added to a_int, but the next
        # time we do the modulus operation, b_int will be zero,
        # and we'll get 0 instead of 10. To avoid this, we subtract
        # 10 from b_int before adding it to a_int.
        b_int -= 10
        if b_int >= 10:
            break

    return numbers