
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
    def exchange_list(lst1, lst2):
        """
        Exchanges the contents of lst1 with lst2.
        """
        lst1[:] = lst2
    
    def is_even(lst):
        """
        Returns True if all the elements of lst are even.
        """
        return all(i % 2 == 0 for i in lst)
    
    def exchange_if_possible(lst1, lst2):
        """
        Performs the exchange between lst1 and lst2 if it is possible.
        Returns the new lst1.
        """
        if len(lst1) < len(lst2):
            lst1, lst2 = lst2, lst1
        
        length = len(lst2)
        
        if is_even(lst1):
            return lst1
        
        exchange_list(lst1, lst2)
        
        if is_even(lst1[:length]):
            return lst1
        
        lst1[:] = [0] * length
        
        return lst1
    
    if len(lst1) == 0 or len(lst2) == 0:
        return False
    
    if len(lst1) != len(lst2):
        return False
    
    return exchange_if_possible(*(sorted(lst1, key=lambda x: -x)))
