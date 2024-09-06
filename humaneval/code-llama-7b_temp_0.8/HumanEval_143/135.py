
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
    #################
    # PSEUDOCODE
    # SPLIT THE WORDS INSIDE THE SENTENCE IN A LIST
    # GO THROUGH EACH WORD
    # CHECK IF WORD IS A PRIME NUMBER
    # IF IT IS, ADD IT TO A NEW LIST
    # JOIN THE WORDS IN THE NEW LIST WITH A SPACE AND RETURN IT
    #################
    sentence = sentence.split()
    new_sentence = []
    for word in sentence:
        prime_nums = []
        if is_prime(len(word)):
            prime_nums.append(word)
        new_sentence.append(word)
    
    return " ".join(new_sentence)
    
