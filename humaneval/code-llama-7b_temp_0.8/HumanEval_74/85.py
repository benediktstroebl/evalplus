
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
    # create a function to count number of characters in string
    def str_count(x):
        y = 0
        for i in x:
            y += len(i)
        return y

    # if the first list is empty, return empty list
    if lst1 == []:
        return []
    # if the second list is empty, return first list
    if lst2 == []:
        return lst1
    # create 2 variables to store number of characters in each list
    num1, num2 = str_count(lst1), str_count(lst2)
    # if the total number of characters in the first list is less than the second list, return first list
    if num1 < num2:
        return lst1
    # if the total number of characters in the second list is less than the first list, return second list
    elif num2 < num1:
        return lst2
    # if the two lists have the same number of characters, return the first list
    else:
        return lst1
