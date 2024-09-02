from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    notes: List[str] = []
    current_beat = 0
    for note in music_string:
        # If the note is the next one in the string and it is not the last beat
        if not music_string[note + 1].startswith('|'):
            # Count the beats for this note
            if music_string[note] == 'o':
                count = 4
            elif music_string[note] == '|':
                count = 2
            else:
                count = 1
            # Add the count of beats to the current beat
            current_beat += count
        # If this is the last beat, move to the next line
        elif music_string[note + 1].startswith('|'):
            current_beat += 1
            break
        # If the note is the last one in the line, move to the next line
        else:
            current_beat += 1
            break
        # Add the note to the notes list
        notes.append(music_string[note])
    return [current_beat] + [1 for i in range(1, len(notes)) if notes[i] != '']

