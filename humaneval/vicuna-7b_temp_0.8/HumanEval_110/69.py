
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
    # loop through the elements of both lists
    for i in range(len(lst1)):
        # check whether the element at index i in lst1 can be exchanged with an element in lst2
        # that is less than or equal to the element at index i in lst1
        # if so, swap the elements and continue to the next iteration
        for j in range(len(lst2)):
            if i - j >= 0:
                if lst1[i] <= lst2[j]:
                    lst1.pop(i)
                    lst2.insert(j, lst1.pop(lst1.index(lst1[i])))
                    break
    return lst1 == [n for n in range(len(lst1)) if n % 2 == 0]