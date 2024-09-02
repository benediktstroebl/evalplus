
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
    # define all possible combinations of words
    combinations = []
    current_combination = []
    for i in range(len(sentence)):
        # append the current word
        current_combination.append(sentence[i])
        # append a space
        current_combination.append(" ")
        # append the next word if it's not empty
        if i < len(sentence) - 1:
            current_combination.append(sentence[i+1])
        else:
            # append an empty string
            current_combination.append("")
    # iterate through all combinations
    for combo in current_combination:
        for j in range(len(combo)):
            # check if the length of the current word is prime
            is_prime = True
            while j < len(combo) and (combo[j] == ' ' or combo[j] == "'"):
                j += 1
            if len(combo[j:]) == 1:
                is_prime = False
            if is_prime:
                combinations.append(combo[j:])
                current_combination[j] = " "
                j += 1
    # get the new sentence
    new_sentence = ""
    for i in range(len(combinations)):
        new_sentence += combinations[i]
    # reverse the order of the words
    new_sentence = new_sentence[::-1]
    return new_sentence