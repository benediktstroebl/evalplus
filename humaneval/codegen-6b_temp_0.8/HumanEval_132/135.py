
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
    letters = []
    for letter in string:
        if letter not in letters and letter != '[' and letter != ']':
            letters.append(letter)
        else:
            if letter == '[':
                letters.append(letter)
            else:
                letters.pop()
    if len(letters) > 0:
        return False
    else:
        return True
    

