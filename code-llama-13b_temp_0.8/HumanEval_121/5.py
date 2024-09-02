
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Even positions start from index 0
    i = 0
    # Odd positions start from index 1
    j = 1
    # Make a list of all the values that are at an even position
    lst_even = lst[::2]
    # Make a list of all the values that are at an odd position
    lst_odd = lst[1::2]
    # Sum the odd values at odd positions
    s = sum(i for i in lst_odd if i % 2 == 1)
    print(f'Sum of the odd values at odd positions: {s}')
    
    # Sum the values of the even positions
    print(sum(lst_even))
    # Add the sums together
    return s + sum(lst_even)
