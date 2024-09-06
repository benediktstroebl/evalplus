

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # минимальная длина подстроки должна быть меньше длины строки, иначе
    # подстрока совпадет с самой собой за счет пересечения
    if len(substring) >= len(string):
        return 0
    count = 0
    for i in range(len(string)):
        idx = string.find(substring, i)
        if idx != -1:
            count += 1
    return count

