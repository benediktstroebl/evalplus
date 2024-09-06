def parse_music(music_string: str) -> List[int]:
    res = list(parser(music_string))
    return res if len(res) else [0]