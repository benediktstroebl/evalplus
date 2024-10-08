def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Create an empty list to hold the even digits
    even_digits = []

    # Loop through the range of numbers between a and b (inclusive)
    for num in range(a, b+1):

        # Convert the number to a string and loop through its digits
        for digit in str(num):

            # Check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:

                # Add the digit to the list
                even_digits.append(int(digit))

    # Sort the list and return it
    return sorted(even_digits)
