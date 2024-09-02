
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
    if lst1 == [] or lst2 == []:
        return "NO"
    exchange_counter = 0
    # Iterate over lst1. If it contains an odd number, we'll have to exchange with lst2
    # If it contains an even number, we don't have to exchange with lst2
    for item in lst1:
        if item % 2 == 1:
            if exchange_counter < len(lst2):
                lst1[exchange_counter], lst2[exchange_counter] = lst2[exchange_counter], lst1[exchange_counter]
                exchange_counter += 1
            else:
                return "NO"
    # If we've gotten here, that means there were no odd numbers in lst1.
    # We can just return "YES"
    return "YES"
