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
    # Extract the string in the format of 'o o| .| o| o| .| .| .| .| o o'
    # and split into list of notes
    notes = music_string.split('|')

    # Initialize an empty list to store the notes
    note_list = []

    # Iterate through each note
    for note in notes:
        # Check if the note is 'o'
        if note == 'o':
            # If it is an 'o' note, append it to the note_list
            note_list.append(4)
        elif note == 'o|':
            # If it is a 'o|' note, append its beats to the note_list
            beats = 2
            while beats > 0:
                note_list.append(beats)
                beats = beats - 1
        else:
            raise ValueError("Invalid note: " + note)

    return note_list