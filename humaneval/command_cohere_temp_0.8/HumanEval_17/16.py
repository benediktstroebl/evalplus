```python
from typing import List

 patterned_notes = r'(?P<whole_notes>\bo\b)(?P<half_notes>\bov\b)(?P<quarter_notes>\bdot\b)?'
 parser = lambda music: parse_notes(music.replace('o|', 'W').replace('.|', 'H').replace('o', 'D'))

def parse_notes(notes_string: str) -> List[int]:
    """INPUT: A string representing musical notes in a special ASCII format.
    OUTPUT: A list of integers corresponding to how many beats each note last."""
    if not notes_string:  return []
    whole_note, half_note, quarter_note = map(int, [(m.group('whole_notes')) * 4, 
                                                  (m.group('half_notes')) * 2,
                                                  (m.group('quarter_notes')) * 1 
                                                  ] if re.search(patterned_notes, notes_string)  else [0, 0, 0])
    return [whole_note] + [half_note] * 2 + [quarter_note] * 3
```