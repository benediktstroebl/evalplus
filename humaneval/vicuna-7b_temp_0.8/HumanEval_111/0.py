
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # Convert the input string to a list of characters
    characters = list(map(str.lower, test))

    # Initialize the dictionary with the most common character as its value
    most_common = characters.pop()
    frequency = {most_common: 1}

    # Loop through the remaining characters and increment the frequency of the most common character
    for char in characters:
        frequency[char] = frequency.get(char, 0) + 1

    # Update the most common character to be the most common character in the dictionary
    most_common = max(frequency, key=frequency.get)

    return frequency[most_common]
