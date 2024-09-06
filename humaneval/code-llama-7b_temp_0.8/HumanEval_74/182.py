
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # make a dictionary of the list with the sum of the chars
    total_dict = {}
    for item in lst1:
        sum = 0
        for char in item:
            sum += ord(char)
        total_dict[item] = sum

    for item in lst2:
        sum = 0
        for char in item:
            sum += ord(char)
        if item in total_dict:
            if total_dict[item] > sum:
                total_dict.pop(item)
            elif total_dict[item] < sum:
                total_dict[item] = sum
        else:
            total_dict[item] = sum

    ans = []
    for key in total_dict:
        ans.append(key)

    return ans
