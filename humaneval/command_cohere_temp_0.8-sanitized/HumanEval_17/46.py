regex = f'{pattern}(?: {pattern})?'
def parse_music(music_string: str) -> List[int]:
    return [4 if m == 'o' else 2 if m == 'o|' else 1 for m in re.findall(regex, music_string)]