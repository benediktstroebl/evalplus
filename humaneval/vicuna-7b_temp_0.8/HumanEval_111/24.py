
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
    # Make a copy of the input string to avoid modifying the original
    test = list(test)
    if not test:
        return {}

    seen_letters = set()
    counts = {}
    for letter in test:
        if letter not in seen_letters:
            seen_letters.add(letter)
            counts[letter] = 1

    remaining_counts = dict((letter, counts[letter]) for letter in counts)
    # We now have the counts of each letter in the original string, but we want the counts
    # of each letter in the original string, but we want the counts with any duplicates removed
    sorted_letters = sorted(counts.keys())
    for letter in sorted_letters:
        if letter in remaining_counts:
            remaining_counts[letter] = remaining_counts[letter] - counts[letter]
            for i in range(remaining_counts[letter]):
                remaining_counts[letter] -= 1
    return remaining_counts

