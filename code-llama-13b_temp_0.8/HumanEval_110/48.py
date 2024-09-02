
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
    if len(lst1) == 0 or len(lst2) == 0:
        return None

    def count_odd_numbers(lst):
        odd = 0
        for num in lst:
            if num % 2 == 1:
                odd += 1
        return odd

    odd_in_first_lst = count_odd_numbers(lst1)
    even_in_first_lst = len(lst1) - odd_in_first_lst

    odd_in_second_lst = count_odd_numbers(lst2)
    even_in_second_lst = len(lst2) - odd_in_second_lst

    if even_in_first_lst >= odd_in_second_lst:
        return "YES"
    else:
        return "NO"

