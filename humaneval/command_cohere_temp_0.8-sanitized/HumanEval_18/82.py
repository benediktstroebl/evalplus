def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string) 
    i = 0
    while i + sub_len <= str_len:
        if string[i:i+sub_len] == substring:
            count += 1
        i += 1
    return count