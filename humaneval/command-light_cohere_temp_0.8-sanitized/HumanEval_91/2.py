def is_bored(sentence):
    return sum(1 for word in sentence.isupper()) == 4