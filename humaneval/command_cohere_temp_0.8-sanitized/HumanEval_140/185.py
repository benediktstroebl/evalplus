def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)