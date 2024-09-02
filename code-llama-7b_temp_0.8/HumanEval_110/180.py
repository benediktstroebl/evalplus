
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
    # A boolean flag that controls the exchange of elements
    # between lst1 and lst2.
    is_exchange_needed = False

    for i in range(len(lst1)):
        # Check if lst1[i] is not even.
        if lst1[i] % 2 != 0:
            # Check if lst2 has even number to exchange with lst1[i].
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    # Exchange elements between lst1[i] and lst2[j].
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    # Set the flag to True to record the exchange.
                    is_exchange_needed = True
                    # Break from the j loop.
                    break

            # If lst2 doesn't have even number to exchange with
            # lst1[i], then we need to return "NO" because
            # we can't make lst1[i] even.
            if not is_exchange_needed:
                return "NO"

    # Iterate over lst1 again to check if all the elements
    # are even now.
    for elem in lst1:
        # If there is even number in lst1, then return "NO"
        # because we can't exchange elements between lst1 and lst2.
        if elem % 2 == 0:
            return "NO"

    # If we reach here, then lst1 contains only even numbers,
    # so we return "YES".
    return "YES"

