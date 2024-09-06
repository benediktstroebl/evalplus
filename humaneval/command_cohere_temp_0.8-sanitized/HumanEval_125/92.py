def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != [''] else len(min(txt.lower(), key=lambda x: (x.count('z'), x.count('a'))))