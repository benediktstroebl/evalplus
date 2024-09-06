
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
    # Initialize dictionary
    d = {}
    
    # Split string by space
    strings = test.split()
    
    for string in strings:
        # Get the first letter
        letter = string[0]
        
        # Add the letter to the dictionary
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
            
    # Initialize list
    letters = []
    
    # Get the maximum letter
    max_letter = max(d, key=lambda x: d[x])
    # Get the maximum value
    max_value = d[max_letter]
    
    for key, value in d.items():
        # Check if the letter is the maximum letter
        if key == max_letter:
            # Check if the letter occurs as many times as the maximum value
            if value == max_value:
                # Add it to the list
                letters.append(key)
            # Check if the letter occurs more times than the maximum value
            elif value > max_value:
                # Clear list
                letters.clear()
                # Add it to the list
                letters.append(key)
            # Check if the letter occurs less times than the maximum value
            else:
                continue
        # Check if the letter is not the maximum letter
        else:
            continue
            
    # Return the list
    return letters
