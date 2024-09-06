def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)