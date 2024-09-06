
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    # an exchange is possible if lst1 contains at least one even number
    # and lst2 contains at least one odd number
    # if an exchange is possible, then all the elements of lst1 should be
    # even numbers and all the elements of lst2 should be odd numbers
    # if the lists are not empty, and all the elements of lst1 are odd numbers
    # and all the elements of lst2 are even numbers, then there is no exchange
    # possible

    # if lst1 does not contain any even numbers, return "NO"
    # if lst2 does not contain any odd numbers, return "NO"

    # set a flag that will be set to "YES" if lst1 contains an even number
    even_flag = "NO"

    # set a flag that will be set to "YES" if lst2 contains an odd number
    odd_flag = "NO"

    # run through both lists
    for element in lst1:

        # if the element is even
        if element % 2 == 0:

            # set the even flag to "YES"
            even_flag = "YES"

    for element in lst2:

        # if the element is odd
        if element % 2 == 1:

            # set the odd flag to "YES"
            odd_flag = "YES"

    # if the even flag is "YES" and the odd flag is "NO"
    if even_flag == "YES" and odd_flag == "NO":

        # return "YES"
        return "YES"

    # if the even flag is "NO" and the odd flag is "YES"
    elif even_flag == "NO" and odd_flag == "YES":

        # return "NO"
        return "NO"

    # if the even flag is "NO" and the odd flag is "NO"
    elif even_flag == "NO" and odd_flag == "NO":

        # run through both lists
        for element in lst1:

            # if the element is odd
            if element % 2 == 1:

                # return "NO"
                return "NO"

        # run through both lists
        for
