
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
    #check if there is an opening bracket
    if string.find('[') == -1:
        return False
    #check if there is no closing bracket
    if string.find(']') == -1:
        return False
    #brackets counter
    brackets_counter = 0
    #check if there is no opening bracket
    if string.find('[') == 0:
        return False
    #check if there is closing bracket
    if string.find(']') == -1:
        return False
    #check if the inside of the brackets is a closed bracket
    for i in range(len(string)):
        if string.find('[') == 0:
            brackets_counter +=1
        elif string.find(']') == -1:
            return False
        elif string.find(']') != -1:
            brackets_counter -= 1
        if brackets_counter < 0:
            return False
    return True
