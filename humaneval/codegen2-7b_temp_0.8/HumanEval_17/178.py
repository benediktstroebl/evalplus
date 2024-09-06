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
    music = music_string.split()
    music_as_ints = [ord(char) for char in music]
    parsed_music = []
    for note_index, note in enumerate(music_as_ints):
        if note == '.':
            parsed_music.append(music_as_ints[note_index+1])
        elif note == '|':
            parsed_music.append(music_as_ints[note_index+1])
            parsed_music.append(music_as_ints[note_index+1])
    return parsed_
