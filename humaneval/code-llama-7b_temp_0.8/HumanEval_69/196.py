
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

    # the goal is to find the most frequent number
    # in other words, the most frequent number should be greater than the count of itself

    # returns -1 if there is no such a number
    # returns the most frequent number if there is such a number

    mostFrequentNumber = -1

    # dictionary: stores the occurrences of each number
    # in other words, number as a key, and its count as the value
    occurrences = {}

    # iterate through the list
    for i in lst:
        # if the number is already in the dictionary, increment its count
        # else, add it to the dictionary
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    # iterate through the dictionary
    # if there is a number that is greater than 0 and has a count greater than or equal to itself
    # update the variable mostFrequentNumber
    for key in occurrences:
        if occurrences[key] >= key:
            mostFrequentNumber = key

    return mostFrequentNumber
