from typing import List
pattern = '^ {0,2}(?:o|o|.|o|o|.|o|o|.) ({1,3}) *$'
def parse_music(music_string: str) -> List[int]:
    output_list = []
    for note in music_string.strip():
        if re.match(pattern, note):
            output_list.append(4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else 0)
    return output_list