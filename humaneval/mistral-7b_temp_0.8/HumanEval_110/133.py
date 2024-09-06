
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
    # base case
    if len(lst1) == 0:
        return 'YES'
    if len(lst2) == 0:
        return 'NO'
    # write your code here
    # fill in the blanks
    # no. of elements in lst1 that are even
    even_elements1 = 0
    # for loop to iterate over the elements in lst1
    for i in range(len(lst1)):
        # if the element is even, increment the even_elements1 count
        if lst1[i] % 2 == 0:
            even_elements1 += 1
    # no. of elements in lst2 that are even
    even_elements2 = 0
    # for loop to iterate over the elements in lst2
    for i in range(len(lst2)):
        # if the element is even, increment the even_elements2 count
        if lst2[i] % 2 == 0:
            even_elements2 += 1
    # if the no. of even elements in lst1 is less than or
