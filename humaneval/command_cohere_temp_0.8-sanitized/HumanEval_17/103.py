from typing import List
Pattern = str
Beat = int
def parse_music(music_string: Pattern) -> List[Beat]:
    """Input to this function is a string representing musical notes in a special ASCII format. 
 Your task is to parse this string and return list of integers corresponding to how many beats does each
note last. 

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

Examples:
parse_music('o o| .| o| o| .| .| .| .| o o')
=> [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

parse_music('o|o|oo|oo|ooo|o|o')
=> [2, 2, 2, 2, 2, 1, 1, 1, 1]
"""

    # Define a dictionary that maps pattern to beat
    beat_mapping = {
        "o": 4,
        "o|": 2,
        ".|": 1,
    }

    # List to store the beats
    beats = []

    # Iterate over each character in the music string
    for char in music_string:
        if char in beat_mapping:
            beats.append(beat_mapping[char])

    # Optional: If the input has 1D lists of notes, this code will also work
    # beats = []
    # for note in music_string:
    #     if isinstance(note, list):
    #         beats.extend(parse_music(note))
    #     else:
    #         beats.append(beat_mapping[note])

    return beats