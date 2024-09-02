
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    # 对每个字符串进行拆分
    str_lst = lst[0].split()
    str_lst.extend(lst[1].split())
    # 拆分的字符串是否已经被使用
    used = [False] * len(str_lst)
    # 记录拆分的字符串数目
    count = 0
    while count < len(str_lst):
        # 如果是第一个为'('，则去掉第二个
        if str_lst[count] == '(':
            if count+1 < len(str_lst):
                str_lst.pop(count+1)
            count += 1
            continue
        # 如果是后一个为'('，则去掉前一个
        elif str_lst[count+1] == '(':
            str_lst.pop(count)
            count += 1
            continue
        # 如果是第一个为')'，则去掉后一个
        elif str_lst[count] == ')':
            if count-1 >= 0:
                str_lst.pop(count-1)
            count += 1
            continue
        # 如果是后一个为')'，则去掉前一个
        elif str_lst[count+1] == ')':
            str_lst.pop(count)
            count += 1
            continue
        # 如果是其他，则直接加1
        else:
            count += 1
            continue
    return 'Yes' if len(str_lst) == 0 else 'No'

