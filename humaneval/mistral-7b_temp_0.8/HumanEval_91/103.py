
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # find length of string
    num_boredom = 0
    for i in range(len(S)):
        if S[i] == "I":
            #find i'th index of i
            found_i = S.find("I", i)
            #find the next index after i
            next_index = S.find(".", found_i + 1)
            #find the index of question mark
            question_mark = S.find("?", found_i + 1)
            #find the index of exclamation point
            exclamation_point = S.find("!", found_i + 1)
            #find the index of the last character in the sentence
            last_char = S.find(".", found_i + 1, len(S))
            #if no question mark, no exclamation point or no period, not boring
            if (question_mark == -1 and exclamation_point == -1 and last_char == -1) or (next_index != -1 and next_index == found_i):
                continue
            #if there
