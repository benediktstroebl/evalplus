
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
    # Openers = []
    # Closers = []
    # for i in string:
    #     if i == '[':
    #         Openers.append('[')
    #     elif i == ']':
    #         Closers.append(']')
    # print(Openers)
    # print(Closers)

    # for i in range(0, len(Openers)):
    #     if i in Closers:
    #         Closers.remove(i)

    # print(Closers)

    for i in string:
        if i == '[':
            Openers.append('[')
        elif i == ']':
            Closers.append(']')
            if len(Openers) == 0:
                return False
            elif len(Openers) > 0 and i < Openers[-1]:
                Openers.pop()
            elif len(Openers) > 0 and i > Openers[-1]:
                return False
    if len(Openers) == 0:
        return True
    else:
        return False

    # print(Openers)
    # print(Closers)

