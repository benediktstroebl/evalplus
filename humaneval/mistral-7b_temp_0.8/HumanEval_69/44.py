
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
    # TODO: Write your code here
    lst_freq = dict()
    for i in lst:
        if i not in lst_freq.keys():
            lst_freq[i] = 0
        lst_freq[i] += 1
    freq_values = list(lst_freq.values())
    values = list(lst_freq.keys())
    freq_values.sort(reverse = True)
    values.sort()
    i = 0
    while i < len(freq_values):
        if freq_values[i] >= values[i]:
            return values[i]
        i += 1
    return -1


