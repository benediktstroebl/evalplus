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
    # Create an empty list to store the beats
    beats = []

    # Get the number of notes in the string
    n_notes = int(music_string[0])

    # Iterate through each note
    for i in range(n_notes):
        # Get the note type (o, |, or .) and the number of beats
        note_type, beats_str = music_string[i*2:i*2+2].split('|')

        # Parse the beats string
        beats_list = parse_beats_list(beats_str)

        # Add the parsed beats to the list
        beats += beats_list

    return beats
