
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
    # your code here
    odd_list = []
    even_list = []
    final_list = []

    # O(n)
    for num in lst1:
        if num % 2 != 0:
            odd_list.append(num)
        else:
            even_list.append(num)

    # O(m)
    for num in lst2:
        if num % 2 != 0:
            final_list.append(num)

    # O(n)
    for num in even_list:
        final_list.append(num)

    # O(m)
    for num in final_list:
        if num % 2 == 0:
            odd_list.remove(num)

    # O(n)
    for num in odd_list:
        if num % 2 != 0:
            return "NO"

    return "YES"

