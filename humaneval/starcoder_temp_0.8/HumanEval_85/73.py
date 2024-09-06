
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    even_numbers = [num for num in lst if num % 2 == 0]

    odd_index_even_numbers = [even_numbers[i] for i in range(0, len(even_numbers), 2)]

    return sum(odd_index_even_numbers)

