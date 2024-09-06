def parse_music(music_string: Pattern) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format. 
 Your task is to parse this string and return list of integers corresponding to how many beats does each
note last. 

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

Example:
'o o| .| o| o| .| .| .| .| o o'
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
"""

    whole_note, half_note, quarter_note = 4, 2, 1

    beats = []
    for note in music_string:
        if note == 'o':
            beats.append(whole_note)
        elif note == 'o|':
            beats.append(half_note)
        elif note == '.|':
            beats.append(quarter_note)
        else:
            beats.append(0)

    return beats