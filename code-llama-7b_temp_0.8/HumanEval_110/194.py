
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

    def is_even(element):
        return element % 2 == 0

    def is_even_list(lst):
        return all(is_even(element) for element in lst)

    lst1_even = [element for element in lst1 if is_even(element)]
    if len(lst1_even) == len(lst1):
        return "YES"

    for element in lst1:
        if not is_even(element):
            lst1.remove(element)

            lst2_even = [element for element in lst2 if is_even(element)]
            if lst1_even == lst1 and is_even_list(lst2_even):
                return "YES"

            lst2.append(element)

    return "NO"

