
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

    if not test:
        return {}
    if len(test) == 1:
        return {test[0] : 1}

    result = {}
    last_letter = test[0]
    current_count = 1
    for current_letter in test[1:]:
        if current_letter == last_letter:
            current_count += 1
        else:
            if last_letter in result:
                if current_count > result[last_letter]:
                    result = {last_letter : current_count}
                elif current_count == result[last_letter]:
                    result[last_letter] = current_count
            else:
                result[last_letter] = current_count

            last_letter = current_letter
            current_count = 1

    if last_letter in result:
        if current_count > result[last_letter]:
            result = {last_letter : current_count}
        elif current_count == result[last_letter]:
            result[last_letter] = current_count
    else:
        result[last_letter] = current_count

    return result
