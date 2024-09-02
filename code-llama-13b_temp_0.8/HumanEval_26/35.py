from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # total=len(numbers)
    # index=0
    # while(index<total):
    #     while(index+1<total):
    #         if(numbers[index]==numbers[index+1]):
    #             numbers.pop(index+1)
    #             total-=1
    #         else:
    #             break
    #     index+=1

    # return numbers
    seen = set()
    return [x for x in numbers if x not in seen and not seen.add(x)]

