
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
    # Initialize a set to store the numbers in lst1.
    num_set = set(lst1)
    # Loop over each number in lst1.
    for num in lst1:
        # If the number is odd, then it is impossible to make lst1 a list
        # of only even numbers.
        if num % 2 == 1:
            return "NO"
        # If the number is even, remove it from the set, and add it to the
        # list of even numbers.
        num_set.remove(num)
        lst2.append(num)
    # If all the numbers in lst1 are even numbers, then all the numbers
    # in the set has to be odd numbers. Therefore, lst2 has to be a list
    # of odd numbers.
    if num_set == set(lst2):
        return "YES"
    else:
        return "NO"
