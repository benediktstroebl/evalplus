
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
    all_even = True
    for num in lst1:
        if num % 2 == 1:
            all_even = False

    if all_even:
        return "YES"

    for i, num in enumerate(lst1):
        if num % 2 == 1:
            for j, num2 in enumerate(lst2):
                if num2 % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]

    all_even = True
    for num in lst1:
        if num % 2 == 1:
            all_even = False

    if all_even:
        return "YES"
    else:
        return "NO"
