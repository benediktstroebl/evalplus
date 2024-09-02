
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # A dictionary to store the count of n-digit positive integers that
    # start or end with 1
    count = {}
    # A list of n-digit positive integers
    list1 = [str(x) for x in range(1, n + 1)]
    # Iterating through each element of the list
    for x in list1:
        # If the element is 1, adding 1 to the count
        if x == 1:
            count[str(x)] = count.get(str(x), 0) + 1
        # If the element is not 1 and its last digit is 1, adding 1 to the
        # count
        elif x != 1 and str(x)[-1] == '1':
            count[str(x)] = count.get(str(x), 0) + 1
    return count
