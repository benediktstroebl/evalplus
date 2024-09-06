import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in the music string
    pattern = re.compile(r'o|' +
                          r'(.)|' +
                          r'o\|' +
                          r'(.)|' +
                          r'.|' +
                          r'o|.' +
                          r'{2,}',
                        flags=re.I)

    # Creating a list to store beats
    beats = []

    # For each match of the regular expression...
    for match in pattern.finditer(music_string):
        # ...checking the length of the previous match to determine the beats
        if match.group(1) == 'o':
            beats.append(4)
        elif match.group(1) == match.group(3):
            beats.append(1)
        else:
            beats.append(2)

    return beats