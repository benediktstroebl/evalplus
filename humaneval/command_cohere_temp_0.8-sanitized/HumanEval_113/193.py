def number_of_odd_digits(strings):
    return [str(len(list(filter(lambda d: d % 2 == 1, s))))
            for s in strings]
def odd_count(lst):
    return number_of_odd_digits(lst)