
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Check if the list is empty or not
    if not lst:
        return 0
    # Store all the even numbers in an empty list
    evens = []
    # If the list is not empty then check if the first element is odd
    if lst[0] % 2 == 1:
        evens.append(lst[0])
        lst = lst[1:]
    # Keep track of the sum
    sum = 0
    # Loop through the list
    for num in lst:
        # Add the current number to the sum if it is odd and even position is not reach
        if num % 2 != 0 and (num - 1) not in evens:
            sum += num
            evens.append(num - 1)
        # If the last element is odd then add it to the sum
        if num % 2 == 1:
            sum += num
    return sum
