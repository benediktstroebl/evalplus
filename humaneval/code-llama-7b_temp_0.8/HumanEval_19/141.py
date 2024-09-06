from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()

    def convert_to_int(s: str) -> int:
        """
        Helper function to convert string to int
        """
        return {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }.get(s)

    def sort_numbers_helper(nums: List[int]) -> List[int]:
        """
        Helper function to sort numbers
        """
        if len(nums) == 1:
            return nums

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[::-1]
            else:
                return nums

        mid = len(nums) // 2
        left = sort_numbers_helper(nums[:mid])
        right = sort_numbers_helper(nums[mid:])
        return sort_helper(left, right)

    def sort_helper(left, right):
        """
        Helper function to merge two sorted list
        """
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res += left[i:]
        if j < len(right):
            res += right[j:]
        return res

    int_numbers = [convert_to_int(num) for num in numbers]
    sorted_nums = sort_numbers_helper(int_numbers)
    return " ".join([str(num) for num in sorted_nums])

