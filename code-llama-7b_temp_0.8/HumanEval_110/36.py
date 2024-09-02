
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
    # find out if there is an odd number in the first list, if so, return "No"
    odd = any(elem%2 for elem in lst1)
    if odd:
        return 'NO'
    # initialize variables to track number of swaps between the two lists
    swap_counter = 0
    # keep going as long as there is an element to swap
    while True:
        # initialize a flag variable to track if there is a match
        match_flag = False
        # loop over the first list
        for i in range(len(lst1)):
            # if element at index i in the first list is even
            if lst1[i] % 2 == 0:
                # loop over the second list
                for j in range(len(lst2)):
                    # check if element at index j in the second list is odd and is not already swapped
                    if lst2[j] % 2 == 1 and lst2[j] not in lst1:
                        # perform the swap
                        lst2[j], lst1[i] = lst1[i], lst2[j]
                        # set the flag variable to True to indicate a match was made
                        match_flag = True
                        # increment the swap counter
                        swap_counter += 1
                        # break out of the inner loop
                        break
        # if we reached the end of the while loop and didn't have a match, there is no way to make the first list all even
        if not match_flag:
            return 'NO'
    return 'YES'
