def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string = string.lower()
    substring = substring.lower()
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == substring:
            count += 1
    return count