
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
    sentence_tokens = sentence.split()
    sentence_length = len(sentence_tokens)
    prime_numbers = []
    
    for index in range(1, sentence_length+1):
        for num in range(2, index+1):
            if index % num == 0:
                break
        else:
            prime_numbers.append(index)
    
    return " ".join(sentence_tokens[prime_numbers.index(len(prime_numbers)) : ])
