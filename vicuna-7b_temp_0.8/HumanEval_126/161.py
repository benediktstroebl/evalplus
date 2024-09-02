
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
    if len(lst) == 1 or (lst[0] != lst[1] and lst[0] != lst[2]):
        return True
    else:
        return False

for number in numbers:
    if is_sorted(numbers):
        print("The number is a prime number.")
    elif is_prime(number):
        print("The number is a prime number.")
    elif is_even(number):
        print("The number is an even number.")
    elif is_odd(number):
        print("The number is an odd number.")
    else:
        print("The number is neither a prime, even, nor odd number.")