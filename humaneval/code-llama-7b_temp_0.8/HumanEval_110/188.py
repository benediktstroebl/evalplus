
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

    def even(number):
        return number % 2 == 0

    def odd(number):
        return number % 2 != 0

    def exchange(lst1, lst2):
        # 1. Find the index of the first element of lst1 that is even.
        first_even_element_index_lst1 = None
        for index, element in enumerate(lst1):
            if even(element):
                first_even_element_index_lst1 = index
                break

        # 2. Find the index of the first element of lst2 that is odd.
        first_odd_element_index_lst2 = None
        for index, element in enumerate(lst2):
            if odd(element):
                first_odd_element_index_lst2 = index
                break

        # 3. If the indexes found in steps 2 and 3 are equal, then
        # we can perform an exchange between lst1 and lst2.
        # Otherwise, the exchanges are impossible.
        if first_even_element_index_lst1 == first_odd_element_index_lst2:
            return "YES"
        else:
            return "NO"

    return exchange(lst1, lst2)

