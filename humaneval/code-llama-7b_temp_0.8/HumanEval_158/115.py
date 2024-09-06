
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # 0. Find the length of the longest string.
    # 1. Loop through the strings and count the number of unique characters in each string.
    # 2. Compare the number of unique characters with the longest one.
    # 3. If there is a new longest string, store it.

    # Store the longest string with 0 unique characters
    longest = None
    # Store the length of the longest string
    longest_len = 0
    # Store the length of the current string
    current_len = 0
    # Store the number of unique characters in the current string
    num_unique = 0

    # Loop through each word
    for word in words:
        # Check if the word is longer than the longest one
        if len(word) > longest_len:
            # If it is, store it.
            longest = word
            longest_len = len(word)
            # Reset the number of unique characters
            num_unique = 0
            # Loop through each character in the word
            for char in word:
                # Check if the character is already in the set
                if char in set(word):
                    # If it is, increase the number of unique characters
                    num_unique += 1

        # Check if the word is the same length as the longest one
        elif len(word) == longest_len:
            # Loop through each character in the word
            for char in word:
                # Check if the character is already in the set
                if char in set(word):
                    # If it is, increase the number of unique characters
                    num_unique += 1

        # If the word is shorter than the longest one, continue
        else:
            continue

        # Check if the number of unique characters is higher than the highest number in this string
        if num_unique > current_len:
            # If it is, store it
            current_len = num_unique
        # Otherwise, ignore it
        else:
            continue

    return longest

