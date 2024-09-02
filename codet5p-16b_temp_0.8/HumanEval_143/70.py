
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    import string
    import re
    import math
    
    sentence = sentence.split()
    new_sentence = ''
    
    for word in sentence:
        
        if word in string.ascii_letters:
            word = word.lower()
            new_sentence = new_sentence + word
        else:
            continue

    new_sentence = re.findall(r'\b\w+\b', new_sentence)
    new_sentence = list(dict.fromkeys(new_sentence))
    
    for word in new_sentence:
        if math.sqrt(len(word)) % 1 == 0:
            continue
        else:
            new_sentence.remove(word)
    
    return''.join(new_sentence)
