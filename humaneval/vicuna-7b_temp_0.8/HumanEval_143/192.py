
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
    # use a dictionary to store words and their lengths
    word_lengths = {}
    
    # iterate through the sentence
    for word in sentence:
        # check if the word is in the dictionary
        if word.upper() in word_lengths:
            # if it is, get its length and add 1 to it
            length = word_lengths[word.upper()]
            words = [word.upper()]
            while len(words) < length:
                # if the current word is not prime, find the first prime number
                # greater than its length
                i = len(words)
                while words[i] != length and i > 0:
                    i -= 1
                j = len(words) - 1
                while j >= 0 and words[j] != length and j > i:
                    j -= 1
                if i == len(words) - 1:
                    # if the current word is prime, add it to the list
                    words.append(words[i])
                else:
                    # if the current word is not prime, add its first prime factor
                    # to the list
                    p = factors(length - 1)[1]
                    words.append(p)
                    for i in range(len(words) - 1):
                        words[i] = words[i] + p
            # add the words to the result
            result = " ".join(words)
            word_lengths[result] = len(result) + 1
            # remove the word from the dictionary
            del word_lengths[word.upper()]
            break
    return result