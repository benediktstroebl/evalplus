from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    ans1 = ''
    ans2 = ''
    for i in numbers:
        if i == '0':
            ans1 += i
        if i == '1':
            ans1 += i
            ans2 += i
        if i == '2':
            ans1 += i
            ans2 += i
        if i == '3':
            ans1 += i
            ans2 += i
        if i == '4':
            ans1 += i
        if i == '5':
            ans1 += i
        if i == '6':
            ans1 += i
        if i == '7':
            ans1 += i
        if i == '8':
            ans1 += i
        if i == '9':
            ans1 += i
    ans = sorted(ans1)
    ans += sorted(ans2)
    return ''.join(ans)

