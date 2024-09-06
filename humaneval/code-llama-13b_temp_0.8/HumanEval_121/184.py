
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Check to see if list has 1 or more elements
    if len(lst) >= 1:
        # Check to see if list has 2 or more elements
        if len(lst) >= 2:
            # Check to see if element at 0th index is odd
            if lst[0] % 2 != 0:
                # Check to see if element at 0th index is even
                if lst[0] % 2 == 0:
                    # Check to see if element at 1st index is odd
                    if lst[1] % 2 != 0:
                        # Check to see if element at 1st index is even
                        if lst[1] % 2 == 0:
                            # Since both elements are even, return the sum
                            return lst[0] + lst[1]
                        # Since 0th element is even and 1st element is odd, return 0th element
                        else:
                            return lst[0]
                    # Since 0th element is odd and 1st element is even, return 1st element
                    else:
                        return lst[1]
                # Since 0th element is even, return 0
                else:
                    return 0
            # Since 0th element is odd, return 0
            else:
                return 0
        # Since there is only 1 element, return 0
        else:
            return 0
    # Since list has no elements, return 0
    else:
        return 0
