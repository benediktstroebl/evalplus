from typing import List
def sort_numbers(input_numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_numbers.split()
    sorted_numbers = 'zero' if numbers[0] == 'one' else 'one'
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:  # skip duplicate entries
            if numbers[i] < numbers[i - 1]:
                sorted_numbers += ' '.join(numbers[i:i + 2])
            else:
                temp = numbers[i]
                numbers[i] = numbers[i - 1]
                numbers[i - 1] = temp
                sorted_numbers += ' '.join(numbers[i:i + 2])
                # return the sorted string with numbers sorted from smallest to largest
                # e.g. input -> 'three one five' , sorted -> 'one three five'
    return sorted_numbers