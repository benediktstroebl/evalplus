
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
    if is_even(lst1):
        return "NO"

    even_lst = [x for x in lst1 if is_even(x)]

    num_of_elements_in_even = len(even_lst)
    num_of_elements_in_lst1 = len(lst1)
    num_of_elements_to_add = num_of_elements_in_lst1 - num_of_elements_in_even

    while num_of_elements_to_add > 0:
        num_of_elements_to_add -= 1

        if is_even(lst1[num_of_elements_in_even]):
            return "NO"

        lst1[num_of_elements_in_even] += 1

    return "YES"

