

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    #Alternate Solution:
    #l' = [0]*len(l)
    #for i in range(len(l)):
    #    l'[2*i] = l[i]
    #    l'[2*i + 1] = l[i]
    #return l'.sort()'

    #Explanation
    #In the first for loop, the idea is that we will construct a copy of l', and then
    #we will mutate the copy, mutating the copy's values to the even indicies and sorting
    #the new l', and replacing the old l, with the new l.

    #The second for loop, takes a copy of l' and sorts it. This is not a copy, but the
    #same list object. Although this does not change the old list, it does change the
    #copy's values. As a result, we have the old list's value sorted into the new list,
    #which we computed by replacing the values of the old list which have been sorted,
    #with the values of the new sorted list.
    
    l2 = []
    for i in range(len(l)):
        l2.append(l[i])
        l2.append(l[i])
    return l2.sort()
