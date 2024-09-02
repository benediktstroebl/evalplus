
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
    # Get the sum of the elements in lst1 and lst2.
    lst1_sum = sum(lst1)
    lst2_sum = sum(lst2)

    # Check if the sums of the elements in lst1 and lst2 are odd or even.
    if lst1_sum % 2 == 0 and lst2_sum % 2 == 0:
        # Check if the sum of lst1 is equal to the sum of lst2.
        if lst1_sum == lst2_sum:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
