from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats
    LEG = ['o', 'o|', '.|', '---|']  # the legend of the notation

    music_list = [[] for _ in range(len(LEG))]  # initialize list of empty lists

    # build a list of durations, where each index corresponds to the length of the corresponding note
    for char in music_string:
        music_list[LEG.index(char)].append(1)

    # compute the actual duration for each note type
    result = [sum(beat_count) * MOD for beat_count in music_list]
    return result