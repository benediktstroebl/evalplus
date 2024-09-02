
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
    def even_filter(lst):
        """Return True if all elements of the list are even."""
        for elem in lst:
            if elem % 2 != 0:
                return False
        return True
    
    def exchange_helper(lst1, lst2):
        """Helper function for exchange."""
        if even_filter(lst1):
            return True
        elif even_filter(lst2):
            return True
        
        if len(lst1) == 1:
            return lst1[0] % 2 == 0
        
        first_half, second_half = lst1[:len(lst1)/2], lst1[len(lst1)/2:]
        
        if exchange_helper(first_half, second_half):
            return True
        elif exchange_helper(second_half, first_half):
            return True
        else:
            return False
    
    return exchange_helper(lst1, lst2)


assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"

