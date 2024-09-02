
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
    odd_numbers = [i for i in lst1 if i % 2 != 0]
    odd_numbers_copy = [i for i in lst1 if i % 2 != 0]
    even_numbers = [i for i in lst1 if i % 2 == 0]
    odd_numbers_copy.extend(even_numbers)

    for odd_number in odd_numbers:
        if odd_number in lst2:
            odd_numbers.remove(odd_number)
            even_numbers.append(odd_number)
            lst2.remove(odd_number)

    lst1 = even_numbers
    lst2 = odd_numbers_copy

    odd_numbers = [i for i in lst1 if i % 2 != 0]
    odd_numbers_copy = [i for i in lst1 if i % 2 != 0]
    even_numbers = [i for i in lst1 if i % 2 == 0]
    odd_numbers_copy.extend(even_numbers)

    for odd_number in odd_numbers:
        if odd_number in lst2:
            odd_numbers.remove(odd_number)
            even_numbers.append(odd_number)
            lst2.remove(odd_number)

    lst1 = even_numbers
    lst2 = odd_numbers_copy

    if len(lst1) == 0:
        return "YES"
    else:
        return "NO"


