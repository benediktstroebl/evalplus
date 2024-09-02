
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
    char_dict = {}
    for item in lst1:
        for char in item:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    for item in lst2:
        for char in item:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    lst = []
    for key, value in char_dict.items():
        if value == min(char_dict.values()):
            lst.append(key)
    return [i for i in lst1 if i.count(lst[0]) == min(list(map(lambda x: x.count(lst[0]), lst1)))]
