def count_distinct_characters(string: str) -> int:
    string = string.lower() 
    distinct_characters = set(string)
    return len(distinct_characters)