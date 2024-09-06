def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list to store the digits of the number from the second to the last
    # This will be the number without the first and last digit
    digits = list(str(n - 1))
    # Remove the last element from the list of digits
    digits.pop()
    # If n is 1, there is only one number which is "1"
    if n == 1:
        return 1
    # If the last digit of the number is 1, the first digit can be anything from 1 to 9
    if digits[-1] == 1:
        return 9
    # If the last digit of the number is not 1, the first digit have to be 1
    # So the number of such numbers is 9 - 1 = 8
    else:
        return 8