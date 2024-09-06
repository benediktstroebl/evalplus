from typing import List
pattern = '^(?:o(?!\\|)|(?:o)?|\\|?) (?=\\.|$)'
def parse_music(music_string: str) -> List[int]:
    return [4 if m == 'o' else 2 if m == 'o|' else 1 for m in music_string.split(' | ') if m and (m[0] in 'o|.') and re.match(pattern, m)]