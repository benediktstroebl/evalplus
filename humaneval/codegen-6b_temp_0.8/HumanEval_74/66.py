
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
    if len(lst1) == 0:
        return lst1
    elif len(lst2) == 0:
        return lst2
    else:
        if len(lst1) < len(lst2):
            return total_match(lst2, lst1)
        else:
            return total_match(lst1, lst2)
            
for x in range(0,5):
    for y in range(0,5):
        for z in range(0,5):
            if(x + y + z <= 5):
                print(total_match(['x', 'y', 'z'][:x], ['v', 'w', 'u'][:y], ['t', 's', 'p'][:z]) )
            
            