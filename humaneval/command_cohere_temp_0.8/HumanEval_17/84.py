```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return list of integers corresponding to how many beats does each
note last.

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

"""
 diplom_music_regex = r'(?P<whole>\bo\b)(?P<half>\b(?:[.|o|])\b)?(?P<quarter>\b(?:[.|o|])\b)?'
 hole_note = 4

def parse_note(note: str) -> int:
    """Returns the number of beats a single note lasts."""
    if note == 'o':
        return hole_note
    elif note == 'o|':
        return hole_note // 2
    elif note == '.|':
        return 1
    else:
        return 0


def parse_music_logic(music_string: Pattern) -> List[int]:
    """The main function parsing the music string."""
    beat_lengths = []
    for note in re.findall(diplom_music_regex, music_string):
        beat = parse_note(note)
        beat_lengths.append(beat)
    return beat_lengths

def parse_music_(music_string: str) -> List[int]:
    """Prettier function for parsing music string."""
    beat_lengths = parse_music_logic(music_string)
    return beat_lengths

# Test Cases
def test_note():
    """Test function for parse_note function."""
    assert parse_note('o') == 4
    assert parse_note('o|') == 2
    assert parse_note('.|') == 1
    assert parse_note('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_note('o o| .| o| o| .| .| .| .| o') == [4, 2, 1, 2, 2, 1, 1, 1, 1]

def test_music_string():
    """Test function for parse_music_logic function."""
    assert parse_music_logic('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music_logic('o o| .| o| o| .| .| .| .| o') == [4, 2, 1, 2, 2, 1, 1, 1, 1]
    assert parse_music_logic('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music_('o o| .| o| o| .| .| .| .| o') == [4, 2, 1, 2, 2, 1, 1, 1, 1]
```