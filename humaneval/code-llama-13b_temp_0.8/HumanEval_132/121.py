
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # return True if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested
    list_string = list(string)
    # remove all empty brackets
    list_string = [x for x in list_string if x not in ['[', ']']]
    # if there is no items in the list, then no brackets are nested
    if len(list_string) == 0:
        return False
    # get the last item from the list, this is the first '['
    last_item = list_string.pop()
    # while the list_string is not empty
    while list_string:
        # pop the last item
        item = list_string.pop()
        # if the item is ']' then set last_item to '['
        if item == ']':
            last_item = '['
        # if the item is '[' then see if the last_item is '['
        else:
            if last_item == '[':
                return True
            else:
                last_item = item
    # if there are no valid subsequence of brackets, then return false
    return False

