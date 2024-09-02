
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
    def check(lst1, lst2):
        """
        Checks if it is possible to make lst1 a list of only even numbers
        by exchanging elements between lst1 and lst2
        :param lst1: a list of numbers
        :param lst2: a list of numbers
        :return: True if possible, False otherwise
        """
        # Check if the size of lst1 is less than or equal to 2
        if len(lst1) <= 2:
            return True
        elif len(lst1) == 2:
            # Check if both elements of lst1 are even
            if lst1[0] % 2 == 0 and lst1[1] % 2 == 0:
                return True
            else:
                return False
        else:
            # Check if the first element of lst1 is even
            if lst1[0] % 2 == 0:
                # Check if the second element of lst1 is greater than the first element
                if lst1[1] > lst1[0]:
                    # Check if the second element of lst1 is odd
                    if lst1[1] % 2 == 1:
                        return True
                    else:
                        return False
            else:
                # Check if the second element of lst1 is even
                if lst1[1] % 2 == 0:
                    # Check if the first element of lst1 is greater than the second element
                    if lst1[0] > lst1[1]:
                        # Check if the first element of lst1 is odd
                        if lst1[0] % 2 == 1:
                            return True
                        else:
                            return False
                else:
                    return False

    # Check if it is possible to exchange elements between lst1 and lst2
    if check(lst1, lst2):
        return "YES"
    else:
        return "NO"