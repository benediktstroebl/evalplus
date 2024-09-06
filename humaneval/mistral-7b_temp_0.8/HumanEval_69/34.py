
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    largest_number = 0
    most_common_number = 1
    most_common_number_frequency = 1
    for number in lst:
        if number > largest_number and number > most_common_number_frequency:
            most_common_number = number
            most_common_number_frequency = lst.count(number)
        elif number == largest_number and number == most_common_number_frequency:
            most_common_number_frequency += lst.count(number)
    if largest_number == 0:
        largest_number = most_common_number
    if largest_number == most_common_number and most_common_number_frequency == 1:
        return -1
    else:
        return largest_number
