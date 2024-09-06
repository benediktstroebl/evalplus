def split_words(txt):
    # Split on commas or spaces, if either character exists
    words = txt.split(',') if ',' in txt or ' ' in txt else None
    # Check if the input is alphabetic characters only and return the count of odd letters
    if not words and txt.isalpha():
        words = sum(1 for char in txt if char.islower() and ord(char) % 2 == 1)
    return ['???'] if words is None else words