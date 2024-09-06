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

    def count_beats(s: str) -> int:
        """This function takes a string as input and returns the number of beats it contains.
        It does so by counting the number of consecutive "o" characters.
        """
        return sum(1 for char in s if char == 'o')

    def parse_notes(s: str) -> List[int]:
        """This function takes a string as input and returns a list of integers representing the
        number of beats each note lasts.
        It does so by splitting the string into pairs of notes and returning a list of their lengths.
        """
        pairs = s.split('|')
        lengths = [pair.count('o') for pair in pairs]
        return lengths

    def note_duration(s: str) -> int:
        """This function takes a string as input and returns the duration of the note it represents.
        It does so by mapping the note types to their corresponding durations in the input string.
        """
        mapping = {
            'o': 1,
            'o|': 2,
            '.|': 1
        }
        return mapping.get(s[0], 1)

    def beat_duration(s: str) -> int:
        """This function takes a string as input and returns the duration of the beat it represents.
        It does so by mapping the note types to their corresponding durations in the input string.
        """
        mapping = {
            'o': 4,
            'o|': 2,
            '.|': 1
        }
        return mapping.get(s[0], 1)

    notes = parse_notes(music_string)
    return [beat_duration(s) for s in notes]

