from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # 1. 对字符串进行去空格操作
    paren_string = paren_string.replace(' ', '')
    # 2. 将字符串转换为list
    paren_list = [c for c in paren_string]
    # 3. 定义一个空列表
    res = []
    # 4. 将首字符追加到res列表中
    res.append(paren_list[0])
    # 5. 获取字符串长度
    str_len = len(paren_list)
    # 6. 循环遍历字符串
    for i in range(1, str_len):
        # 7. 如果当前字符不是左括号且不是右括号
        if paren_list[i] != '(' and paren_list[i] != ')':
            # 8. 继续遍历
            continue
        # 9. 如果当前字符是左括号且上一位是右括号
        if paren_list[i] == '(' and paren_list[i - 1] == ')':
            # 10. 将当前字符追加到res列表中
            res.append(paren_list[i])
        # 11. 如果当前字符是右括号且上一位是左括号
        elif paren_list[i] == ')' and paren_list[i - 1] == '(':
            # 12. 将当前字符追加到res列表中
            res.append(paren_list[i])
        else:
            # 13. 如果当前字符不是左括号且上一位不是右括号
            # 14. 如果当前字符是右括号且上一位不是左
