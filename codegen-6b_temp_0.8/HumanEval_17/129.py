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
    # "Vasya: Здесь должна быть версия сортировки, которая работает с многомарштанством
    # алгоритмов и использует одну единственную коллекцию деревьев. В целом, вся же функция может
    # быть логично оптимизирована под некоторую неограниченную реализацию. Однако, если текущую
    # функцию не может оптимизировать, то она будет достаточно глубокой, и по сравнению с кодом
    # (за исключением сортировки слияния и последовательных последовательных попыток), ниже написанной
    # здесь фун