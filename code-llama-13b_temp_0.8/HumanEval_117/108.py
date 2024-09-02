
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # PLAN
    # 1. create a list that contains all the words from s
    # 2. create a list that contains all the words with the correct number of consonants
    # 3. return the correct list

    # 1. create a list that contains all the words from s
    s_list = s.split()

    # 2. create a list that contains all the words with the correct number of consonants
    list_with_correct_number_of_consonants = []
    for i in range(len(s_list)):
        if str(s_list[i]).isalpha() == False:
            continue
        else:
            consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
            for letter in str(s_list[i]):
                if letter not in consonant_list:
                    consonant_list.append(letter)
            if len(consonant_list) == n + 1:
                list_with_correct_number_of_consonants.append(s_list[i])
    
    # 3. return the correct list
    return list_with_correct_number_of_consonants
