
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # Write your code here.
    # Convert n to string and split it into a list of digits
    digits = list(str(n))
    # Create two empty lists to store digits in different positions
    first_digits = []
    last_digits = []

    # Iterate over the digits and append them to the appropriate list
    for digit in digits:
        if len(digits) == 1:
            first_digits.append(digit)
            last_digits.append(digit)
        elif len(digits) == 2:
            first_digits.append(digit)
            last_digits.append(digit)
        else:
            first_digits.append(digit)
            last_digits.append(digit)

    # Calculate the number of integers that start with 1
    for digit in first_digits:
        if digit == '1':
            count += 1

    # Calculate the number of integers that end with 1
    for digit in
