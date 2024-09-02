
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

    # step 1 - extract the data
    # step 2 - what's the goal
    # step 3 - devise a plan
    # step 4 - execute the plan

    # Step 1 - extract the data
    str_ = test
    # Step 2 - what's the goal
    # goal is to count the letters in the string and return the count in a dictionary
    # Step 3 - devise a plan
    # step 3a - define the variables
    #    histogram = {}
    # step 3b - devise the algorithm
    #    1. take the string apart
    #    2. count the letters
    #    3. return the count in a dictionary
    # step 3c - implement the plan
    str_ = test
    histogram = {}
    for letter in str_:
        if letter not in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    return histogram


    # step 1 - extract the data
    # step 2 - what's the goal
    # goal is to count the letters in the string and return the count in a dictionary
    # Step 3 - devise a plan
    # step 3a - define the variables
    #    histogram = {}
    # step 3b - devise the algorithm
    #    1. take the string apart
    #    2. count the letters
    #    3. return the count in a dictionary
    # step 3c - implement the plan
    # step 4 - execute the plan
