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

    def parse_note(note: str) -> int:
        beat = {'o': 4, 'o|': 2, '.|': 1}.get(note)
        if beat is None:
            raise ValueError(f"Unknown note: {note}")
        return beat

    beats = []
    current_beat = 0
    for note in music_string:
        beat = parse_note(note)
        current_beat += beat
        beatsappend= beats.append(current_beat)

    return beats