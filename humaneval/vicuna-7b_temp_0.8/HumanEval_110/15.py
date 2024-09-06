
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
    # Define a variable "e" to store the elements of the even numbers in the first list
    even_e = []

    # Iterate through the first list and store the elements that are even in the variable "even_e"
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            even_e.append(lst1[i])

    # If there are any even numbers in the first list, return "YES"
    if len(even_e) > 0:
        return "YES"
    else:
        return "NO"

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 5, 3, 4]

print(exchange(lst1, lst2))
