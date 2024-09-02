
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # TODO: Use the modulo operator to determine if a number starts or ends
    # with 1
    # TODO: Use the integer division operator to determine if a number has 1
    # as its first or last digit
    # TODO: Use the string operator to determine if a number is less than or
    # greater than 10
    # TODO: Use the addition operator to increment an integer
    # TODO: Use the multiplication operator to multiply an integer by 10
    # TODO: Use the addition operator to add two integers
    # TODO: Use the subtraction operator to subtract two integers
    # TODO: Use the comparison operator to compare two integers
    # TODO: Use the boolean operators to determine if a condition is met
    # TODO: Use the if statement to check whether a condition is met
    # TODO: Use the for loop to iterate through a list
    # TODO: Use the range() function to generate a range of integers
    # TODO: Use the list() function to create a list from an iterable
    # TODO: Use the len() function to get the length of a list
    count = 0
    for i in range(100000):
        if i % 10 == 1 or i / 10 == 1 or i / 100 == 1:
            count += 1

    return count
