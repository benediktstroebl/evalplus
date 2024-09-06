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
    last_note_beat = 0
    notes = []
    for i in range(0, len(music_string), 2):
        if music_string[i] == "o":
            last_note_beat += 1
            notes.append(1)
        elif music_string[i] == "o|":
            last_note_beat += 0.5
            notes.append(0.5)
        elif music_string[i] == ".":
            last_note_beat += 0.25
            notes.append(0.25)
        # print(f"last_note_beat: {last_note_beat}")
    return notes

