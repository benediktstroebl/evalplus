def histogram(test):
    """Return a dictionary of the most repetitive letters and their counts.
    
    Args:
        test (str): Space separated lowercase letters.
        
    Returns:
        dict: A dictionary containing the most frequent letters and their counts.
    """
    hist = {}
    for c in test.split():
        hist[c] = hist.get(c, 0) + 1

    max_count = max(hist.values())
    result = {}
    for letter, count in hist.items():
        if count == max_count:
            result[letter] = count

    return result