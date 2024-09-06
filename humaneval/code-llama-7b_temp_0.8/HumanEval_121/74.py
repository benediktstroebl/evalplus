
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # assign first and second elements of list to variables
    first = lst[0]
    second = lst[1]
    # create variables for index and sum
    index = 0
    sum = 0
    # while loop to iterate through list
    while index < len(lst):
        # if the index is even and the value is odd, add to sum
        if index % 2 == 0 and first % 2 == 1:
            sum += first
        # if the index is odd and the value is odd, add to sum
        elif index % 2 == 1 and second % 2 == 1:
            sum += second
        # increment index
        index += 1
        # assign first and second elements of list to variables
        first = lst[index]
        second = lst[index + 1]
    # return sum
    return sum

