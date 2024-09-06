
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # if there is only one odd number in the list, it must be in an even position, so return the sum of the other elements
    if sum(lst)%2 != 0:
        return sum(lst)
    # otherwise, check for the presence of two odd numbers, which must be in consecutive positions
    if sum(lst)%2 == 0 and sum(lst)%4 == 0:
        return max(lst[1:]) + sum(lst[0:1])
    # if there is no such pair of odd numbers, check for the presence of more than one odd number in the list
    for i in range(1, len(lst)):
        if sum(lst[:i]) % 2 != 0 and sum(lst[:i]) % 4 != 0:
            # there is an odd number in position i, but there is no odd number in position i-1
            if lst[i] > lst[i-1]:
                # if the odd number in position i is the last odd number in the list, return the sum of the other elements
                if i == len(lst)-1:
                    return sum(lst[0:i])
                # otherwise, return the sum of the elements from i to the end of the list
                else:
                    return sum(lst[i:])
            # otherwise, there is an odd number in position i-1, but there is no odd number in position i
            else:
                # there is an odd number in position i-1, but there is no odd number in position i
                if lst[i] > lst[i+1]:
                    # if the odd number in position i-1 is the last odd number in the list, return the sum of the other elements
                    if i == 0:
                        return sum(lst[1:])
                    # otherwise, return the sum of the elements from i-1 to the end of the list
                    else:
                        return sum(lst[i-1:])
                # otherwise, there is no such pair of odd numbers, so return 0
                else:
                    return 0
    # if none of the above cases apply, return 0
    else:
        return 0
