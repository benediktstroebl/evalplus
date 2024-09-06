from collections import OrderedDict
def remove_duplicates(numbers: List[int]) -> List[int]:
    dup_dict = OrderedDict()
    result = []
    for num in numbers:
        if num not in dup_dict:
            dup_dict[num] = True
            result.append(num)
    return result