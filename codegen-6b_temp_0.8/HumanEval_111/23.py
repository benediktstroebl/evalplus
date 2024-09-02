
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
    test = test.split()
    
    def get_duplicates(test):
        """
        Returns all duplicates in a list of strings.
        
        """
        return set(string for string in test if test.count(string) > 1)
    
    def all_same_char(test, char):
        """
        Returns True if all characters are the same in the given string
        
        """
        return all(char == item for item in test)
    
    duplicates = get_duplicates(test)
    hist = {}
    
    for item in duplicates:
        new_hist = {}
        
        # iterate over the list of duplicate items
        # and add the count of the occurrence to the new dictionary
        for i in range(0, len(item)):
            new_hist[item[i]] = hist.get(item[i], 0) + 1
            
            # iterate over the dictionary of exemplars of each type of letter
            # and increment the occurrence count per type
            for exemplar, count in hist.iteritems():
                new_hist[exemplar] = new_hist.get(exemplar, 0) + 1
            
        # finally add the new dictionary to the dictionary of exemplars
        hist.update(new_hist)
    
    return hist
