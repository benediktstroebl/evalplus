def how_many_times(string: str, substring: str) -> int:
    count = 0
    idx = 0
    while idx < len(string) - len(substring) + 1:
        if string[idx:idx + len(substring)] == substring:
            count += 1
            idx += 1
        else:
            idx += 1
            if idx + len(substring) > len(string):
                break
    return count