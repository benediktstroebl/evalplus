def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string) 
    idx = 0

    while idx < str_len - sub_len:
        idx = string.find(substring, idx)
        if idx != -1:
            count += 1
            idx += sub_len
        else:
            break

    return count