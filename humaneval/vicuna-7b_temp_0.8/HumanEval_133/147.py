

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    squared_list = [x**2 for x in lst]
    squared_list.append(0)
    squared_list[-1] = round(squared_list[-1], upper_int=True)
    return sum(squared_list)

print(sum_squares([1,2,3,4]))
print(sum_squares([1,4,9]))
print(sum_squares([1,3,5,7]))
print(sum_squares([1.4,4.2,0]))
print(sum_squares([-2.4,1,1]))