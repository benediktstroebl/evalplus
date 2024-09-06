
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

    # Check if list is not empty
    if lst1 and lst2:
        # Declare variables
        is_even = True
        lst1_evens = []
        lst2_odds = []
        # Iterate over lists
        for num in lst1:
            # Check if number is even
            if num % 2 == 0:
                lst1_evens.append(num)
            else:
                is_even = False
        for num in lst2:
            # Check if number is even
            if num % 2 != 0:
                lst2_odds.append(num)
            else:
                is_even = False
        # If both lists contain only even numbers return YES, otherwise return NO
        if is_even:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

