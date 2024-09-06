def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    max_distance = string_length - substring_length  # To account for cases where substring can be at the very end of the string
    
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
            max_distance -= 1
        if max_distance < 0: 
            break
    
    return count