from typing import List
PATTERN = """
    (o|O){beats} 
    |  
    (o|O)|(.|.) 
    {beats} 
    (o|O){beats} 

"""
def parse_music(music_string: str) -> List[int]:
    def match_note(note):
        beat = 4 if note == 'o' else 2
        return beat

    regex = re.compile(PATTERN)
    result = list(map(match_note, regex.findall(music_string)))
    return result