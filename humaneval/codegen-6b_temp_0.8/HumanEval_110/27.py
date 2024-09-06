
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
    # First, find the max number of numbers to exchange
    max_num = len(lst1) # Set to the length of lst1
    for i in range(len(lst2)): # i is a variable to track the position
        if lst2[i] > max_num: # If lst2[i] is larger than max_num
            max_num = lst2[i] # Then set max_num equal to lst2[i]

    # Step 1: Start by making a list of all possible exchanges
    output = []
    for i in range(max_num + 1):
        for j in range(i):
            output.append((j, i - j)) # Append a tuple of the form (j, i-j)

    # Step 2: Check if the two lists are one of these exchanges
    for exchange in output:
        if exchange[0] < len(lst1) and exchange[1] < len(lst1): # If the exchange is possible
            if lst1[exchange[0]] % 2 == 0 and lst1[exchange[1]] % 2 == 0:
                return "YES"
    return "NO"

