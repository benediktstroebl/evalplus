from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # replace spaces with nothing
    parsed_music_string = music_string.replace(' ', '')

    # note: need to loop over parsed_music_string multiple times
    # if you don't do this, it will break on the first occurence

    # because we want to get the first occurence of each note,
    # we need to accumulate all duplicate characters
    note_counts = []
    note_count = 0
    for i in range(len(parsed_music_string)):
        if parsed_music_string[i] not in note_counts:
            note_count += 1
            note_counts.append(parsed_music_string[i])

    # now we have a list of unique characters
    note_counts = [1 for i in range(len(note_counts))]

    # now we can loop over each note and count up the number of beats it lasts for
    counter = 0
    for note_index in range(len(note_counts)):
        # we want to skip the first note (which we already counted)
        note_to_skip = note_counts[note_index]
        # we also want to skip the last note (which we already counted)
        first_note_index = note_index + 1
        last_note_index = len(note_counts) - 1
        last_note = note_counts[last_note_index]

        # now we need to get the index of the first note we don't want to skip
        while first_note_index != last_note_index and first_note_index != last_note_index + 1:
            first_note_index += 1
            if note_to_skip == note_counts[first_note_index]:
                first_note_index -= 1
                break

        # now we know the index of the first note we dont want to skip
        # we know its the last note index and we want to start at the next index
        # of the first note index (since we don't want to skip it)
        counter += 1
        first_note = note_counts[first_note_index]
        while first_note_index != last