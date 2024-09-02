
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
    st = '['
    en = ']'
    f_st = ''
    f_en = ''
    l_st = ''
    l_en = ''
    index = 0
    lst = list(string)
    for i in range(len(lst)):
        if lst[i] == st:
            f_st += st
            f_en += en
            l_st += st
            l_en += en
            index = i
            break
    for j in range(index + 1, len(lst)):
        if lst[j] == st:
            f_st += st
            f_en += en
            l_st += st
            l_en += en
        elif lst[j] == en:
            if l_st[-1] == lst[j]:
                l_st = l_st[:-1]
                l_en = l_en[:-1]
            else:
                return False
        else:
            l_st += st
            l_en += en
    return True if f_
