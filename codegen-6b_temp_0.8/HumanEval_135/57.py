
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # set up a hashmap to track the distance of each element from its predecessor
    # if we reach the last element of the array then index of that element
    # will be the answer
    # if the element to the left of the element is less than its both to the
    # right and to the left of its left neighbour then the distance is
    # right - left - 1
    # if the element to the left of the element to the right of its left
    # neighbour is equal to the right then the distance is right - left
    # if the element to the right of the element left to the right of its
    # right neighbour is equal to the length of the array then the distance
    # is -1
    # if none of the above matches the distance is set to -1
    # if you see a duplicate value you cannot sort the array since you will
    # have to sort it with duplicate values.

    # if we see a duplicate value then we return -1
    # if we see a position at which a greater value is encountered
    # then we return the position of the greater value
    # so we do not have to deal with searching for values greater than our
    # immediate predecessor

    # if we reach the end of the array then the greatest absolute value will be
    # -1 since a number is not greater than itself
    # so we do not need to worry about the -1 case
    # we now know that we will be returning a position
    # of the greatest element
    if len(arr) < 2:
        return -1

    h = dict()
    for i in range(len(arr)):
        if i == 0:
            h[arr[i]] = 0
        elif arr[i] not in h:
            h[arr[i]] = i
        else:
            if arr[h[arr[i]]] > arr[i]:
                return h[arr[i]]
            else:
                return i

    return -1

