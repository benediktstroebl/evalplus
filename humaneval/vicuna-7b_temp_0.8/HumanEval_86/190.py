
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Using a map to store ASCII values of characters
    ascii_map = {ord(c): i for i, c in enumerate(s)}
    # Using a list to store new characters
    new_chars = []
    # Iterating over the characters in the string
    for c in s:
        # If character is in map, add 1 to its index
        if c in ascii_map:
            ascii_map[c] += 1
        # If character is not in map, add it to map with index 0
        else:
            ascii_map[ord('a')] = 0
            ascii_map[ord('z')] = 26
            ascii_map[c] = 27
        # If index exceeds max index of map, set it to max index
        if ascii_map[c] > max(ascii_map.values()):
            ascii_map[c] = max(ascii_map.values())
        # Adding character to new_chars list
        new_chars.append(c)
    return ' '.join(new_chars)
