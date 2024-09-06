
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # We are going to use an optimized approach: Count the letters
    # from the first word. Using this count let's see for each word if we
    # have to increment the count or not.
    letters = {}
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    # Now we sort the letters and iterate through the list.
    # For each letter we see if we have already seen that letter before.
    # If not, we need to increment the count.
    for word in words:
        for letter in word:
            if letters[letter] == 1:
                letters[letter] -= 1
                break
    # Finally we find the word with maximum count of letters.
    max_word = ""
    max_count = 0
    for word in words:
        count = 0
        for letter in word:
            if letters[letter] > 0:
                count += 1
        if count > max_count:
            max_count = count
            max_word = word
    return max_word

