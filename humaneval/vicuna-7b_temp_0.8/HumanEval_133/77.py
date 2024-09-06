

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
    # Creating a list of all the positive numbers in the list
    positive_lst = [x for x in lst if x > 0]
    # Creating a list of all the negative numbers in the list
    negative_lst = [x for x in lst if x < 0]
    # Creating a list of all the zero numbers in the list
    zero_lst = [x for x in lst if x == 0]
    # Adding all the positive numbers and negative numbers and zero numbers
    total_sum = sum(positive_lst) + sum(negative_lst)
    # Using the while loop to iterate through the list and check if the number is positive, negative or zero
    for i in range(len(lst)):
        if lst[i] > 0:
            positive_lst.append(lst[i])
        elif lst[i] < 0:
            negative_lst.append(lst[i])
        else:
            zero_lst.append(lst[i])
    # Using the Ceiling function to round the numbers to the nearest int
    total_sum = total_sum.round(np.ceil)
    # Return the sum of squared numbers
    return total_sum

test = [5,6,7,8,9,20,21,22,23,24,25]
