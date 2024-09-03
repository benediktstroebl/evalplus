def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count