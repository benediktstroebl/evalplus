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
    # Every note has the same length of the quarter note
    quarter_note = 1
    # Some notes have the same length as half or whole notes
    whole_note = quarter_note * 4
    half_note = quarter_note * 2

    # Create a dictionary containing information about the note length
    notes = {"o": whole_note, "o|": half_note, ".|": quarter_note}

    # Replace the music string with one without spaces
    music_string_without_spaces = music_string.replace(" ", "")
    # Convert the string to a list
    music_string_list = list(music_string_without_spaces)

    # Count the number of beats for every note
    beat_length = [notes[x] for x in music_string_list]

    return beat_length

