
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
    lines = test.split("\n")
    count = {}
    for line in lines:
        line = line.strip().lower()
        if line not in count:
            count[line] = 1
        else:
            count[line] += 1
    for line, count in count.items():
        if line not in count.keys():
            print(line, count.get(line, 0))
        else:
            print(f"{line}: {count.get(line, 0)}")
    
