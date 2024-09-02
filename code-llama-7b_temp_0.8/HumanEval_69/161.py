
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

    # 1 - find most frequent number
    # 2 - return most frequent number if >= current number
    # 3 - return -1 if no number > current number
    # 4 - if numbers are same, remove all but one

    # 1 - find most frequent number
    from collections import defaultdict
    freq = defaultdict(int)
    for i in lst:
        freq[i] += 1
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    most_frequent_number = list(freq.keys())[0]
    most_frequent_number_count = freq[most_frequent_number]

    # 2 - return most frequent number if >= current number
    if most_frequent_number_count >= most_frequent_number:
        for i in range(len(lst)):
            if lst[i] == most_frequent_number:
                return most_frequent_number
    # 3 - return -1 if no number > current number
    return -1
