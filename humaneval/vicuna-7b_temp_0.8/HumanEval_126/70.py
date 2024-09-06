
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    def count_unique_numbers(lst):
        unique_numbers = {}
        for num in lst:
            if num in unique_numbers:
                unique_numbers[num] += 1
            else:
                unique_numbers[num] = 1
        return unique_numbers

    def is_sorted_by_unique_numbers(lst):
        num_unique, num_lst = len(count_unique_numbers(lst)), len(lst)
        for i in range(num_lst):
            for j in range(i + 1, num_lst):
                if count_unique_numbers(lst[i:j])[-1] != count_unique_numbers(lst[i:j])[0]:
                    return False
        return True

    return is_sorted_by_unique_numbers(lst)