def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))