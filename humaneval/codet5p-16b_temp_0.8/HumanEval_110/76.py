
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

    # The solution here is to iterate over the input lists. For each element,
    # if the element is even, then we can try to exchange the element with the
    # last element of lst2. If the exchange is valid, then we can remove the
    # last element of lst2 and replace it with the current element.
    if not lst2:
        return "NO"
    for element in lst1:
        if element % 2 == 0:
            last_element = lst2.pop()
            if last_element % 2 == 0:
                exchange(lst1, lst2)
            else:
                lst1.remove(element)
    if not lst1:
        return "YES"
    else:
        return "NO"
